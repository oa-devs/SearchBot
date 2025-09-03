#!/usr/bin/env python3

import os
import sys
import time
import random
import argparse
from datetime import datetime
from typing import List, Tuple

try:
    from googlesearch import search
    import requests
except ImportError:
    print("❌ Missing dependencies. Run: pip install -r requirements.txt")
    sys.exit(1)

class SearchBot:
    
    def __init__(self, queries_file="queries.txt", results_file="results.txt", max_results=5):
        self.queries_file = queries_file
        self.results_file = results_file
        self.max_results = max_results
        self.session_stats = {"queries_processed": 0, "urls_found": 0, "errors": 0}
    
    def setup_queries_file(self) -> None:
        if not os.path.exists(self.queries_file):
            print(f"📝 Creating sample {self.queries_file}")
            with open(self.queries_file, 'w') as f:
                f.write("# SearchBot Queries File\n")
                f.write("# Add your search queries here, one per line\n")
                f.write("# Lines starting with # are comments and will be ignored\n\n")
                f.write("# Example queries:\n")
                f.write("# python web scraping tutorial\n")
                f.write("# machine learning best practices\n")
                f.write("# REST API design patterns\n")
    
    def load_queries(self) -> List[str]:
        self.setup_queries_file()
        
        if not os.path.exists(self.queries_file):
            return []
        
        with open(self.queries_file, 'r', encoding='utf-8') as file:
            queries = [
                line.strip() 
                for line in file 
                if line.strip() and not line.strip().startswith('#')
            ]
        
        print(f"📚 Loaded {len(queries)} queries from {self.queries_file}")
        return queries
    
    def search_query(self, query: str) -> List[str]:
        print(f"\n🔍 Searching: '{query}'")
        urls = []
        
        try:
            for i, url in enumerate(search(query, num_results=self.max_results), 1):
                urls.append(url)
                print(f"  [{i}] {url}")
                time.sleep(random.uniform(0.5, 1.5))
                
        except requests.exceptions.HTTPError as e:
            print(f"❌ HTTP Error: {e}")
            self.session_stats["errors"] += 1
        except Exception as e:
            print(f"❌ Search Error: {e}")
            self.session_stats["errors"] += 1
        
        print(f"✅ Found {len(urls)} URLs")
        return urls
    
    def save_results(self, query: str, urls: List[str]) -> None:
        if not urls:
            return
        
        with open(self.results_file, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"\n# Query: {query}\n")
            f.write(f"# Timestamp: {timestamp}\n")
            f.write(f"# Results: {len(urls)} URLs\n")
            f.write("-" * 50 + "\n")
            
            for url in urls:
                f.write(f"{url}\n")
            f.write("\n")
    
    def run(self, queries: List[str]) -> None:
        if not queries:
            print("⚠️  No queries to process. Add queries to queries.txt")
            return
        
        print(f"🚀 Starting SearchBot with {len(queries)} queries")
        print(f"📁 Results will be saved to: {self.results_file}")
        print("-" * 50)
        
        for i, query in enumerate(queries, 1):
            print(f"\n[{i}/{len(queries)}] Processing query...")
            
            urls = self.search_query(query)
            self.save_results(query, urls)
            
            self.session_stats["queries_processed"] += 1
            self.session_stats["urls_found"] += len(urls)
            
            if i < len(queries):
                delay = random.uniform(2, 4)
                print(f"⏳ Waiting {delay:.1f}s before next query...")
                time.sleep(delay)
        
        self.print_summary()
    
    def print_summary(self) -> None:
        stats = self.session_stats
        print("\n" + "=" * 50)
        print("🎉 SearchBot Session Complete!")
        print(f"📊 Queries processed: {stats['queries_processed']}")
        print(f"🔗 Total URLs found: {stats['urls_found']}")
        print(f"❌ Errors encountered: {stats['errors']}")
        print(f"📁 Results saved to: {self.results_file}")
        print("=" * 50)

def main():
    parser = argparse.ArgumentParser(
        description="SearchBot - Automated web search and URL collection tool"
    )
    parser.add_argument(
        "-q", "--queries", 
        default="queries.txt",
        help="Queries file (default: queries.txt)"
    )
    parser.add_argument(
        "-o", "--output",
        default="results.txt", 
        help="Output file (default: results.txt)"
    )
    parser.add_argument(
        "-n", "--num-results",
        type=int,
        default=5,
        help="Max results per query (default: 5)"
    )
    
    args = parser.parse_args()
    
    bot = SearchBot(
        queries_file=args.queries,
        results_file=args.output,
        max_results=args.num_results
    )
    
    queries = bot.load_queries()
    bot.run(queries)

if __name__ == "__main__":
    print("🤖 SearchBot v1.0 - Automated Web Search Tool")
    main()