import argparse

def main():
    parser = argparse.ArgumentParser()
    
    # Add arguments
    parser.add_argument('input_string', type=str,)
    parser.add_argument('input_int', type=int,)
    parser.add_argument('input_float', type=float,)
    
    # Parse arguments
    args = parser.parse_args()
    
    # Access and print parsed arguments
    print('String:', args.input_string)
    print('Integer:', args.input_int)
    print('Float:', args.input_float)

if __name__ == "__main__":
    main()