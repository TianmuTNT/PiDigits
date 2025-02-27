# PiDigits  

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

A Python program that streams the digits of π (pi) indefinitely, calculated digit-by-digit using Jeremy Gibbons' infinite spigot algorithm.  

## Features  
- Real-time digit-by-digit computation of π.  
- Minimal memory usage (no precomputed values stored).  
- Clean, generator-based implementation for seamless integration into other projects.  

## Usage  

### Prerequisites  
- Python 3.x  

### Running the Program  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/TianmuTNT/PiDigits.git  
   cd PiDigits  
   ```  
2. Run the script:  
   ```bash  
   python3 pi_digits.py  
   ```  
3. The program will print `3.` followed by the decimal digits of π, one by one.  
4. Press `Ctrl+C` to stop execution.  

## Algorithm Details  
This implementation uses the **infinite spigot algorithm** by Jeremy Gibbons. Unlike finite spigot methods, it avoids preallocating memory for all digits and generates them on-the-fly.  

## License  
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.  

## Disclaimer  
**For Educational Purposes Only**  
This code is intended to demonstrate algorithmic concepts and is not optimized for high-performance π computation.  

## Contributing  
Feel free to open issues or submit pull requests for improvements.  

![Star History Chart](https://api.star-history.com/svg?repos=TianmuTNT/PiDigits)
