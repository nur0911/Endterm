#Task 2
def translate_Letter(letter):
    translation_table = {
        'A+': 4.3, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'D-': 0.7
    }
    if letter in translation_table:
        return translation_table[letter]
    else:
        return 0.0


def calculate_GPA(scores, credits):
    total_points = 0
    total_credits = sum(credits)

    for score, credit in zip(scores, credits):
        total_points += translate_Letter(score) * credit

    if total_credits != 0:
        return round(total_points / total_credits, 2)
    else:
        return 0.0


credits_file_path = "credits.txt"
credits_data = []
with open(credits_file_path, 'r') as credits_file:
    for line in credits_file:
        data = line.strip().split()
        if len(data) == 2 and data[1].isdigit():
            credits_data.append(int(data[1]))

course_names = ['math', 'chemistry', 'english']
overall_GPAs = []
for course_name in course_names:
    course_scores_file_path = f"{course_name}.txt"
    scores_data = []
    with open(course_scores_file_path, 'r') as scores_file:
        for line in scores_file:
            scores_data.append(line.strip())

    gpa = calculate_GPA(scores_data, credits_data)
    overall_GPAs.append(f"{course_name}: {gpa}")

overall_GPAs_file_path = "overallGPAs.txt"
with open(overall_GPAs_file_path, 'w') as overall_file:
    overall_file.write("\n".join(overall_GPAs))

print("Overall GPAs saved to 'overallGPAs.txt'")
print("\n")

