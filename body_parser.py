import json

text = """
Acyclic-Graph Directories
• What happen when two users work on same file?
• Common subdirectory should be shared.(shared directory or file two or
more places at once)
• Some programs also needs same file to be place on dif erent directories. • All changes are reflect to both users. • How to implement?
• Using link (another file or subdirectory)
• Duplicate all information about them in both sharing directories. (Issue? dif icult
to keep consistency
"""

# result = json.dumps({"usr":text})
# print(result)


import json

# response = {
#     "questions1": {"ans1": "str", "ans2": "str", "ans3": "str", "ans4": "str", "correct": "str"},
#     "questions2": {"ans1": "str", "ans2": "str", "ans3": "str", "ans4": "str", "correct": "str"},
#     "questions4": {"ans1": "str", "ans2": "str", "ans3": "str", "ans4": "str", "correct": "str"},
#     "questions5": {"ans1": "str", "ans2": "str", "ans3": "str", "ans4": "str", "correct": "str"},
#     "questions6": {"ans1": "str", "ans2": "str", "ans3": "str", "ans4": "str", "correct": "str"},
#     "questions8": {"ans1": "str", "ans2": "str", "ans3": "str", "ans4": "str", "correct": "str"},
#     "questions9": {"ans1": "str", "ans2": "str", "ans3": "str", "ans4": "str", "correct": "str"},
#     "questions15": {"ans1": "str", "ans2": "str", "ans3": "str", "ans4": "str", "correct": "str"},
#     "questions16": {"ans1": "str", "ans2": "str", "ans3": "str", "ans4": "str", "correct": "str"},
# }

response = {
    "questions": [
        {"question": "str", "options": ["str", "str", "str", "str"], "correct": "str"},
        {"question": "str", "options": ["str", "str", "str", "str"], "correct": "str"},
        {"question": "str", "options": ["str", "str", "str", "str"], "correct": "str"},
        {"question": "str", "options": ["str", "str", "str", "str"], "correct": "str"},
        {"question": "str", "options": ["str", "str", "str", "str"], "correct": "str"},
        {"question": "str", "options": ["str", "str", "str", "str"], "correct": "str"},
        {"question": "str", "options": ["str", "str", "str", "str"], "correct": "str"},
        {"question": "str", "options": ["str", "str", "str", "str"], "correct": "str"},
    ]
}

result = json.dumps(response)
print(result)

