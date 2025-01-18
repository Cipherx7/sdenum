### Simplified Description
This script is a **Subdomain Enumeration Tool** designed for ethical hacking and security purposes. It utilizes tools like **Amass**, **Sublist3r**, and **FFUF** to find subdomains of a target domain. The script supports customization of wordlists, combines results from all tools, and saves the output in a unified file. It is beginner-friendly, with clear error messages and usage instructions.

---

### `README.md`

```markdown
# Subdomain Enumeration Tool

## Description
The **Subdomain Enumeration Tool** is designed to help ethical hackers and security enthusiasts enumerate subdomains of a given domain. It integrates with popular tools like **Amass**, **Sublist3r**, and **FFUF**, allowing users to customize wordlists and consolidate results in a single file. 

This tool is user-friendly, provides meaningful error messages, and allows for customization of settings like wordlists, making it versatile for different use cases.

---

## Features
- **Multi-tool Integration**: Supports Amass, Sublist3r, and FFUF for comprehensive subdomain enumeration.
- **Customizable Wordlists**: Set and save custom wordlists for each tool.
- **Error Handling**: Displays a banner and clear error messages if required inputs are missing.
- **Merge Results**: Combines output from all tools into a single file for easy analysis.
- **Quiet Mode**: Suppresses the banner for streamlined operation.

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/subdomain-enum-tool.git
   cd subdomain-enum-tool
   ```

2. Install dependencies:
   - Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Install required tools:
     - **Amass**: Follow installation instructions at [Amass GitHub](https://github.com/OWASP/Amass).
     - **Sublist3r**: Clone and set up [Sublist3r](https://github.com/aboul3la/Sublist3r).
     - **FFUF**: Follow installation instructions at [FFUF GitHub](https://github.com/ffuf/ffuf).

3. Ensure tools are added to your system's PATH or accessible from the terminal.

---

## Usage
Run the tool with the following syntax:
```bash
python3 subdomain.py <domain> [options]
```

### Options:
| Option | Description                                             |
|--------|---------------------------------------------------------|
| `-a`   | Use **Amass** for enumeration.                         |
| `-u`   | Use **Sublist3r** for enumeration.                     |
| `-f`   | Use **FFUF** for enumeration.                          |
| `-w`   | Customize wordlists for each tool.                     |
| `-q`   | Quiet mode (suppress the banner).                      |

### Examples:
1. Enumerate subdomains using all tools:
   ```bash
   python3 subdomain.py example.com
   ```

2. Enumerate subdomains using only Amass:
   ```bash
   python3 subdomain.py example.com -a
   ```

3. Customize wordlists:
   ```bash
   python3 subdomain.py -w
   ```

4. Run quietly with FFUF only:
   ```bash
   python3 subdomain.py example.com -f -q
   ```

---

## Features
1. **Automatic Tool Integration**: Automates the execution of Amass, Sublist3r, and FFUF.
2. **Wordlist Customization**: Allows users to set and save custom wordlists for different tools.
3. **Results Consolidation**: Merges outputs from all tools into a single file for easy reference.
4. **Beginner-Friendly**: Displays a helpful banner and error messages to guide users.
5. **Quiet Mode**: Option to suppress banners for automation or CI/CD pipelines.

---

## To-Do
- Add support for more subdomain enumeration tools.
- Enable multi-threading for faster execution.
- Provide detailed analytics or visualization of results.
- Add Docker support for easier setup.

---

## Examples
### Default Execution:
```bash
python3 subdomain.py example.com
```
Output:
- Amass, Sublist3r, and FFUF will run with default wordlists.
- Results will be saved in `final_output.txt`.

### Customizing Wordlists:
1. Run the tool with the `-w` option:
   ```bash
   python3 subdomain.py -w
   ```
2. Follow the prompts to set custom wordlists for Amass, Sublist3r, and FFUF.
3. Wordlists will be saved and reused for subsequent runs.

### Tool-Specific Execution:
- **Only Amass**:
  ```bash
  python3 subdomain.py example.com -a
  ```
- **Only Sublist3r**:
  ```bash
  python3 subdomain.py example.com -u
  ```
- **Only FFUF**:
  ```bash
  python3 subdomain.py example.com -f
  ```

---

## Output
- **Default File Structure**:
  - `amass_output.txt`: Amass results.
  - `sublist3r_output.txt`: Sublist3r results.
  - `ffuf_output.txt`: FFUF results.
  - `final_output.txt`: Combined results from all tools.

- **Logs**:
  - Errors and informational messages are displayed in the terminal.

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.
```

This `README.md` provides all necessary details to set up, use, and contribute to your tool, while being beginner-friendly. Let me know if you’d like further refinements!
