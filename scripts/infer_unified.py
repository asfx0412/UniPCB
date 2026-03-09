#!/usr/bin/env python3
"""
UniPCB Unified Inference Script
A unified inference interface for multiple MLLMs on PCB quality inspection tasks.

Supports:
- Multiple model backends (Qwen, InternVL, GPT-4V, etc.)
- Standardized input/output formats
- Batch processing with concurrency
- Evaluation metrics computation
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


class UniPCBInference:
    """Unified inference interface for UniPCB benchmark."""
    
    def __init__(
        self,
        model_name: str,
        api_base: str,
        api_key: Optional[str] = None,
        config_path: Optional[str] = None,
        max_workers: int = 10,
        max_pixels: int = 3000000,
    ):
        """
        Initialize inference engine.
        
        Args:
            model_name: Name of the model backend
            api_base: API endpoint URL
            api_key: API key (if required)
            config_path: Path to configuration file
            max_workers: Number of concurrent workers
            max_pixels: Maximum pixels for image processing
        """
        self.model_name = model_name
        self.api_base = api_base
        self.api_key = api_key
        self.max_workers = max_workers
        self.max_pixels = max_pixels
        
        self.config = self._load_config(config_path) if config_path else {}
        
        # Load model-specific configuration
        self.model_config = self.config.get("models", {}).get(model_name, {})
        
        print(f"Initialized {model_name} inference engine")
        print(f"API endpoint: {api_base}")
        print(f"Max workers: {max_workers}")
    
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from file."""
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def load_test_data(self, data_path: str) -> List[Dict]:
        """
        Load test dataset.
        
        Args:
            data_path: Path to test data JSON file
        
        Returns:
            List of test samples
        """
        print(f"Loading test data from: {data_path}")
        
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"Loaded {len(data)} samples")
        return data
    
    def process_sample(self, sample: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a single sample.
        
        Args:
            sample: Test sample with image and question
        
        Returns:
            Model prediction
        """
        try:
            # Extract image and question from sample
            image = self._extract_image(sample)
            question = self._extract_question(sample)
            
            # Generate model response
            response = self._generate_response(image, question)
            
            # Parse response
            parsed = self._parse_response(response)
            
            return {
                "sample_id": sample.get("id", ""),
                "question": question,
                "response": response,
                "parsed_answer": parsed,
                "status": "success"
            }
            
        except Exception as e:
            return {
                "sample_id": sample.get("id", ""),
                "status": "error",
                "error": str(e)
            }
    
    def _extract_image(self, sample: Dict[str, Any]) -> Any:
        """Extract image from sample."""
        # Support multiple image key formats
        for key in ["image", "images", "image_path", "file_name"]:
            if key in sample:
                return sample[key]
        raise ValueError("No image found in sample")
    
    def _extract_question(self, sample: Dict[str, Any]) -> str:
        """Extract question/prompt from sample."""
        # Support multiple prompt formats
        for key in ["question", "prompt", "query", "instruction", "input"]:
            if key in sample:
                return str(sample[key])
        
        # Try conversations format
        if "conversations" in sample:
            conv = sample["conversations"]
            if isinstance(conv, list):
                # Find last human/user message
                for turn in reversed(conv):
                    role = turn.get("from", turn.get("role", "")).lower()
                    if role in ("human", "user"):
                        return turn.get("value", turn.get("content", ""))
        
        raise ValueError("No question found in sample")
    
    def _generate_response(self, image: Any, question: str) -> str:
        """
        Generate response from model.
        
        Args:
            image: Input image
            question: Question/prompt
        
        Returns:
            Model response text
        """
        # Model-specific generation logic
        if self.model_name.lower() in ["qwen", "qwen-vl", "qwen2.5"]:
            return self._generate_qwen(image, question)
        elif self.model_name.lower() in ["internvl"]:
            return self._generate_internvl(image, question)
        else:
            # Generic API call
            return self._generate_generic(image, question)
    
    def _generate_qwen(self, image: Any, question: str) -> str:
        """Qwen-specific generation."""
        # TODO: Implement Qwen API call
        # Placeholder for actual implementation
        return f"Qwen response to: {question}"
    
    def _generate_internvl(self, image: Any, question: str) -> str:
        """InternVL-specific generation."""
        # TODO: Implement InternVL API call
        # Placeholder for actual implementation
        return f"InternVL response to: {question}"
    
    def _generate_generic(self, image: Any, question: str) -> str:
        """Generic API call."""
        # TODO: Implement generic API call
        # Placeholder for actual implementation
        return f"Generic response to: {question}"
    
    def _parse_response(self, response: str) -> Dict[str, Any]:
        """
        Parse model response.
        
        Args:
            response: Raw model response
        
        Returns:
            Parsed answer components
        """
        # Try to extract structured answer
        import re
        
        # Try <answer>...</answer> format
        answer_re = re.compile(r"<answer>(.*?)</answer>", re.S | re.I)
        match = answer_re.search(response)
        
        if match:
            return {
                "answer": match.group(1).strip(),
                "format": "structured",
                "has_answer_tag": True
            }
        
        # Fallback: return entire response
        return {
            "answer": response.strip(),
            "format": "freeform",
            "has_answer_tag": False
        }
    
    def run_inference(
        self,
        data_path: str,
        output_path: str,
        test_mode: bool = False,
        test_samples: int = 10,
    ) -> None:
        """
        Run inference on entire dataset.
        
        Args:
            data_path: Path to test data
            output_path: Path to save results
            test_mode: Run in test mode (process subset)
            test_samples: Number of samples to process in test mode
        """
        # Load data
        test_data = self.load_test_data(data_path)
        
        # Filter for test mode
        if test_mode:
            test_data = test_data[:test_samples]
            print(f"Test mode enabled: processing {len(test_data)} samples")
        
        # Process with concurrency
        results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self.process_sample, sample): sample
                for sample in test_data
            }
            
            for future in tqdm(
                as_completed(futures),
                total=len(futures),
                desc="Running inference"
            ):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    print(f"Error processing sample: {e}")
        
        # Save results
        self._save_results(results, output_path)
        
        # Compute and print statistics
        self._print_statistics(results)
    
    def _save_results(self, results: List[Dict], output_path: str):
        """Save results to file."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"Results saved to: {output_path}")
    
    def _print_statistics(self, results: List[Dict]):
        """Print inference statistics."""
        total = len(results)
        success = sum(1 for r in results if r.get("status") == "success")
        errors = total - success
        
        print("\n" + "="*60)
        print("Inference Statistics")
        print("="*60)
        print(f"Total samples: {total}")
        print(f"Successful: {success} ({success/total*100:.1f}%)")
        print(f"Errors: {errors} ({errors/total*100:.1f}%)")
        
        # Count answer formats
        formats = {}
        for r in results:
            if r.get("status") == "success":
                parsed = r.get("parsed_answer", {})
                fmt = parsed.get("format", "unknown")
                formats[fmt] = formats.get(fmt, 0) + 1
        
        if formats:
            print("\nAnswer Formats:")
            for fmt, count in formats.items():
                print(f"  {fmt}: {count} ({count/success*100:.1f}%)")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="UniPCB Unified Inference")
    
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="Model name (qwen, internvl, gpt4v, etc.)"
    )
    parser.add_argument(
        "--data",
        type=str,
        required=True,
        help="Path to test data JSON file"
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Path to save results"
    )
    parser.add_argument(
        "--api-base",
        type=str,
        default="http://localhost:10029/v1",
        help="API base URL"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=None,
        help="API key (if required)"
    )
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Path to configuration file"
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=10,
        help="Number of concurrent workers"
    )
    parser.add_argument(
        "--test-mode",
        action="store_true",
        help="Run in test mode (process subset of data)"
    )
    parser.add_argument(
        "--test-samples",
        type=int,
        default=10,
        help="Number of samples to process in test mode"
    )
    
    args = parser.parse_args()
    
    # Initialize inference engine
    inference = UniPCBInference(
        model_name=args.model,
        api_base=args.api_base,
        api_key=args.api_key,
        config_path=args.config,
        max_workers=args.max_workers,
    )
    
    # Run inference
    inference.run_inference(
        data_path=args.data,
        output_path=args.output,
        test_mode=args.test_mode,
        test_samples=args.test_samples,
    )


if __name__ == "__main__":
    main()
