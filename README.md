# 📝 NLTK Text Summarizer

A simple Python script for extractive text summarization using NLTK. It selects key sentences from input text based on word frequency analysis.

---

## 🚀 How It Works

1. **Tokenize** text into sentences and words  
2. **Remove** stopwords and punctuation  
3. **Score** sentences by word frequency  
4. **Extract** top 3 most relevant sentences (customizable)

---

## 📦 Requirements

- Python 3  
- `nltk`, `heapq`, `string`

### Install NLTK and download data:

```bash
pip install nltk
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```
## 🧪 Example Usage

### Run the script:

```bash
python summarizer.py
```
Output: A summary of the input text.

## 🛠️ Customization
Change number of summary sentences:
heapq.nlargest(3, ...) → replace 3 with desired count

Adjust sentence length filter in word_count

## 📄 License
This project is licensed under the [MIT License](LICENSE).
