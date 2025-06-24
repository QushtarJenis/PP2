import re

txt = "Contact us at info@example.com or support@domain.org for help."
pattern = r"\b[\w\.-]+@[\w\.-]+\.(?:com|org|net)\b"
x = re.findall(pattern, txt)
print(x)
