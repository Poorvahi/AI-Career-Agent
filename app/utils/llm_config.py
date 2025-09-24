from langchain_openai import ChatOpenAI
from app.configure import OPENAI_API_KEY
import openai


class MockLLM:
    """A fake LLM that returns predictable responses for testing."""
    def invoke(self, inputs):
        # You can customize these mock outputs
        if isinstance(inputs, dict):
            if "interest" in inputs:
                return type("AIMessage", (), {"content": "1. Software Engineer\n2. Data Scientist\n3. Cybersecurity Analyst"})()
            elif "careers" in inputs and "skill" not in inputs:
                return type("AIMessage", (), {"content": "Software Engineer - Platforms: Coursera - https://coursera.org\nData Scientist - Platforms: Kaggle Learn - https://kaggle.com/learn\nCybersecurity Analyst - Platforms: TryHackMe - https://tryhackme.com"})()
            elif "careers" in inputs and "skill" in inputs:
                return type("AIMessage", (), {"content": "Software Engineer - Skills: Python, Problem Solving, Databases - Salary: ₹6-15 LPA\nData Scientist - Skills: Python, Machine Learning, Statistics - Salary: ₹8-20 LPA\nCybersecurity Analyst - Skills: Networking, Security Tools, Risk Analysis - Salary: ₹5-12 LPA"})()
        return type("AIMessage", (), {"content": "Mock response"})()


def get_openai_llm(model="gpt-3.5-turbo"):
    if not OPENAI_API_KEY:
        print("⚠ No API key found — using MockLLM for testing.")
        return MockLLM()

    try:
        return ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            model=model,
            temperature=0.3
        )
    except openai.error.RateLimitError:
        print("⚠ OpenAI quota exceeded, using MockLLM instead.")
        return MockLLM()
    except openai.error.InvalidRequestError as e:
        if "insufficient_quota" in str(e):
            print("⚠ OpenAI API quota exhausted, using MockLLM.")
            return MockLLM()
        raise e
