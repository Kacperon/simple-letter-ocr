import os
import time
import argparse
import sys

try:
    from main import predict_letter
except ImportError as e:
    print(f"BŁĄD: Nie można zaimportować predict_letter z main.py: {str(e)}")
    sys.exit(1)

# Expected letters for images 1-10 (starting from A)
expected_letters = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
    6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J'
}

def run_tests(tests_dir="tests", start_idx=1, end_idx=10, verbose=True):
    """Runs OCR tests on a set of images and evaluates performance"""
    # Sprawdź czy katalog testów istnieje
    if not os.path.exists(tests_dir):
        print(f"BŁĄD: Katalog testów '{tests_dir}' nie istnieje.")
        return None
        
    if verbose:
        print("=== TESTING LETTER RECOGNITION ===")
        print(f"{'Image':<10}{'Predicted':<15}{'Expected':<15}{'Probability':<15}{'Result':<10}")
        print("-" * 65)

    correct_count = 0
    total_tests = 0
    start_time = time.time()
    
    # Test each image from start_idx.jpg to end_idx.jpg
    for i in range(start_idx, end_idx + 1):
        image_path = os.path.join(tests_dir, f"{i}.jpg")
        
        # Skip if file doesn't exist
        if not os.path.exists(image_path):
            if verbose:
                print(f"Warning: Image {i}.jpg not found, skipping.")
            continue
            
        # Predict the letter with error handling
        try:
            letter, probability = predict_letter(image_path)
        except Exception as e:
            if verbose:
                print(f"Error processing image {i}.jpg: {str(e)}")
            continue
        
        # Check if prediction matches expected letter
        expected = expected_letters.get(i, "?")
        result = "✓" if letter == expected else "✗"
        is_correct = letter == expected
        
        if is_correct:
            correct_count += 1
        total_tests += 1
        
        # Print results
        if verbose:
            print(f"{i}.jpg{'':<5}{letter:<15}{expected:<15}{probability:.4f}{'':<10}{result}")
    
    # Calculate metrics
    execution_time = time.time() - start_time
    accuracy = (correct_count / total_tests) * 100 if total_tests > 0 else 0
    
    # Print summary
    if verbose:
        print("-" * 65)
        print(f"Tests completed: {total_tests}")
        print(f"Correct predictions: {correct_count}")
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Execution time: {execution_time:.2f} seconds")

def main():
    """Main function to parse arguments and run tests"""
    parser = argparse.ArgumentParser(description="Test letter recognition system")
    parser.add_argument("--dir", type=str, default="tests", help="Directory containing test images")
    parser.add_argument("--start", type=int, default=1, help="Starting image index")
    parser.add_argument("--end", type=int, default=10, help="Ending image index")
    parser.add_argument("--quiet", action="store_true", help="Suppress detailed output")
    
    args = parser.parse_args()
    
    run_tests(
        tests_dir=args.dir,
        start_idx=args.start,
        end_idx=args.end,
        verbose=not args.quiet
    )

if __name__ == "__main__":
    main()