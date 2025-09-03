# SearchBot

A lightweight Python tool that automates Google searches from a list of queries and saves result URLs for research and analysis.

## Features

- Batch search from `queries.txt` (one query per line)
- Saves organized results to `results.txt` with timestamps
- Randomized delays to reduce rate-limiting
- Command-line interface with options
- Session statistics and error handling
- Clean, object-oriented codebase

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Add queries (one per line)
echo -e "python web scraping\nbest linux distros 2025" > queries.txt

# Run SearchBot
python3 searchbot.py
```

## Command Line Options

```bash
python3 searchbot.py --help                    # Show help
python3 searchbot.py -n 10                     # Get 10 results per query
python3 searchbot.py -q myqueries.txt          # Use custom queries file
python3 searchbot.py -o myresults.txt          # Save to custom output file
```

## File Structure

```
SearchBot/
├── searchbot.py      # Main bot script
├── requirements.txt  # Python dependencies
├── queries.txt       # Search queries (auto-created)
├── results.txt       # Search results (auto-created)
└── README.md        # This file
```

## Example queries.txt

```
# SearchBot Queries File
python web scraping tutorial
machine learning best practices
REST API design patterns
```

## Output Format

Results are saved with metadata including timestamps and query information for easy reference.

## Notes

- Use responsibly and follow search engine terms of service
- Built-in delays help avoid rate limiting
- Results include duplicate detection within sessions
