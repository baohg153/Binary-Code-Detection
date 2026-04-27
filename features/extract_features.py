# This file is not usable anymore, wait for fixing
import re
import math
import zlib
import statistics
import pandas as pd
from collections import Counter

class FeatureExtractor:
    def __init__(self):
        pass

    def extract_line_length_feature(self, code: str):
        if not code or not code.strip():
            return 0.0
        
        lines = code.split('\n')
        non_empty_lines = [len(line) for line in lines if line.strip()]
        if len(non_empty_lines) > 1:
            avg_line_len = statistics.mean(non_empty_lines)
            std_line_len = statistics.stdev(non_empty_lines)
            cv_line_len = std_line_len / avg_line_len if avg_line_len > 0 else 0
        else:
            cv_line_len = 0.0
        
        return round(cv_line_len, 4)

    def extract_word_length_feature(self, code: str):
        if not code or not code.strip():
            return 0.0
        
        words = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)
        if words:
            return round(sum(len(w) for w in words) / (len(words) * 5), 4)
        else:
            return 0.0
        
    
    def extract_blank_line_feature(self, code: str):
        if not code or not code.strip():
            return 0.0
        
        lines = code.split('\n')
        blank_lines = sum(1 for line in lines if not line.strip())
        blank_line_ratio = blank_lines / len(lines) if lines else 0.0

        return round(blank_line_ratio, 4)
    
    def extract_compression_feature(self, code: str):
        if not code or not code.strip():
            return 0.0
        
        code_bytes = code.encode('utf-8')
        compressed_bytes = zlib.compress(code_bytes)
        compression_ratio = len(compressed_bytes) / len(code_bytes)
        
        return round(compression_ratio, 4)

    def extract_word_entropy_feature(self, code: str):
        words = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)
        if words:
            word_counts = Counter(words)
            total_words = len(words)
            
            entropy = 0.0
            for count in word_counts.values():
                p = count / total_words
                entropy -= p * math.log2(p)

            return round((entropy - 3)/2, 4)
        else:
            return 0.0
    
    def extract_features(self, code):
        if not code or not code.strip():
            return [0.0, 0.0, 0.0, 0.0, 0.0]
        
        line_length = self.extract_line_length_feature(code)
        word_length = self.extract_word_length_feature(code)
        blank_line = self.extract_blank_line_feature(code)
        compression = self.extract_compression_feature(code)
        word_entropy = self.extract_word_entropy_feature(code)

        return [line_length, word_length, blank_line, compression, word_entropy]

    def extract_features_from_file(self, input_file: str, output_file: str = ""):
        df = pd.read_parquet(input_file)
        code_list = df["code"].tolist()

        extracted_features = [self.extract_features(code) for code in code_list]
        feature_df = pd.DataFrame(extracted_features, columns=['line_length','word_length','blank_line','compression','word_entropy'])
        if output_file:
            feature_df.to_parquet(output_file)
        
        return extracted_features
    
# Extract features and save to file
feat_extractor = FeatureExtractor()
feat_extractor.extract_features_from_file("../data/test.parquet", "./extracted_features/test.parquet")