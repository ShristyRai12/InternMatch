import pandas as pd
from flask import Flask, render_template, request

from src.recommender import (
    calculate_match,
    get_missing_skills,
    get_matched_skills,
    get_top_recommendations,
    get_skill_priority,
    filter_internships,
    prepare_internships,
    display_recommendations,
    find_invalid_skills
)
app = Flask(__name__)


df=pd.read_csv("data/indian_tech_career_intelligence_2026.csv")
# print(df)
# print(df.shape)
# print(df.columns.tolist())

columns = [
    "job_title",
    "job_category",
    "company_name",
    "location_city",
    "location_state",
    "work_mode",
    "stipend_amount",
    "experience_level",
    "education_required",
    "employment_type",
    "skills_extracted",
    "job_description",
    "application_deadline",
    "source_platform",
    "is_active"
]

df = prepare_internships(df)

#taking only internship jobs
# df = df[df["employment_type"] == "Internship"].copy()
# print("Internships:", len(df))
# print(df["job_title"].value_counts().head(15))
#removing not active internships
# df = df[df["is_active"] == True].copy()
# print("Active Internships:", len(df))
# print(df["skills_extracted"].head(10).to_string(index=False))
# print(df["skills_extracted"].iloc[0])

#converting skills into list
df["skills_list"] = df["skills_extracted"].apply(
    lambda x: [skill.strip().lower() for skill in x.split(",")]
)

# print(df[["job_title", "skills_list"]].head())






# print("\n========== INTERNMATCH ==========")
# print("Find internships based on your skills\n")

# user_input = input("Enter your skills (comma separated): ")

# user_skills = [
#     skill.strip().lower()
#     for skill in user_input.split(",")
#     if skill.strip()
# ]

# if not user_skills:
#     print("Please enter at least one skill.")
#     exit()

# available_skills = set(
#     skill
#     for skills in df["skills_list"]
#     for skill in skills
# )

# invalid_skills = [
#     skill for skill in user_skills
#     if skill not in available_skills
# ]

# if invalid_skills:
#     print("\n⚠️ Skills not found in dataset:")
#     print(", ".join(invalid_skills))
# else:
#     print("\n✓ Skills recognized successfully.")

# if len(invalid_skills) == len(user_skills):
#     print("None of the entered skills were found in the dataset.")
#     exit()

# print("\nSelect your preferences")

# work_mode = input(
#     "Enter preferred work mode (Remote/Hybrid/On-site/Any): "
# ).strip().lower()

# # if work_mode != "any":
# #     df = df[df["work_mode"].str.lower() == work_mode]

# location = input(
#     "Enter preferred city (or Any): "
# ).strip().lower()

# # if location != "any":
# #     df = df[df["location_city"].str.lower() == location]
# df = filter_internships(df, work_mode, location)
# if df.empty:
#     print("No internships found for your selected preferences.")
#     exit()

# df["match_score"] = df["skills_list"].apply(
#     lambda skills: calculate_match(user_skills, skills)
# )

# # print(df["match_score"].describe())


# # recommendations = get_recommendations(user_skills, df)
# # print(
# #     recommendations[
# #         ["job_title", "match_score", "matched_skills", "missing_skills"]
# #     ]
# # )
# df = df.sort_values("match_score", ascending=False)
# # print(df[["job_title", "skills_list", "match_score"]].head(10))
# # top_jobs=df.head(5)
# # print("-------------top 5 jobs based on match score-------------")
# # print(top_jobs)
# df["matched_skills"] = df["skills_list"].apply(
#     lambda skills: get_matched_skills(user_skills, skills)
# )
# # df["matched_skills"] = df["skills_list"].apply(
# #     lambda skills: [skill for skill in skills if skill in user_skills]
# # )
# df["missing_skills"] = df["skills_list"].apply(
#     lambda skills: get_missing_skills(user_skills, skills)
# )
# # df["missing_skills"] = df["skills_list"].apply(
#     # lambda skills: [skill for skill in skills if skill not in user_skills]
# # )
# # print(df[["job_title", "skills_list", "missing_skills"]].head(10))
# # print(len(df["missing_skills"].iloc[0]))

# recommendations = get_top_recommendations(df)
# # recommendations = df.sort_values(
# #     "match_score",
# #     ascending=False
# # ).drop_duplicates(
# #     "job_title"
# # ).head(5)

# # print(recommendations[["job_title", "match_score", "missing_skills","matched_skills"]])
# top_skills = get_skill_priority(recommendations)
# # missing = recommendations["missing_skills"].explode()
# # skill_counts = missing.value_counts()
# # # print(skill_counts)
# # top_skills=skill_counts.head(5)
# # print("-------------top 5 skills to learn for better match-------------")
# # print(top_skills)
# recommendations = recommendations.reset_index(drop=True)

# # print(recommendations["job_title"].duplicated().any()) : to check for duplicates

# final_recommendations = recommendations[
#     ["job_title", "skills_list", "match_score", "missing_skills","matched_skills","job_category", "company_name", "location_city", "location_state", "work_mode", "stipend_amount", "application_deadline"]
# ].copy()
# # print(final_recommendations)
# skill_priority = top_skills.reset_index()
# skill_priority.columns = ["skill", "job_count"]
# # print(skill_priority)
# # print(skill_priority[skill_priority["skill"].isin(user_skills)])

# #creating matched skills column
# df["matched_skills"] = df["skills_list"].apply(
#     lambda skills: [skill for skill in skills if skill in user_skills]
# )
# # print(
#     # df[
#         # ["job_title", "matched_skills", "missing_skills", "match_score"]
#     # ].head(10)
# # )
# # print("\n========== INTERNSHIP RECOMMENDATIONS ==========\n")

# # for i, (_, job) in enumerate(recommendations.iterrows(), start=1):
# #     print(f"Recommendation {i}")
# #     print("-" * 45)
# #     print(f"Job Title        : {job['job_title']}")
# #     print(f"Category         : {job['job_category']}")
# #     print(f"Company          : {job['company_name']}")
# #     print(f"Location         : {job['location_city']}")
# #     print(f"Work Mode        : {job['work_mode']}")
# #     print(f"Stipend          : {job['stipend_amount']}")
# #     print(f"Match Score      : {job['match_score']:.2f}%")
# #     print(f"Matched Skills   : {', '.join(job['matched_skills'])}")
# #     print(f"Missing Skills   : {', '.join(job['missing_skills'])}")
# #     print(f"Application Date : {job['application_deadline']}")
# #     print()
# display_recommendations(recommendations)
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "GET":
        return render_template("index.html")

    user_input = request.form["skills"]

    work_mode = request.form["work_mode"].strip().lower()

    location = request.form["location"].strip().lower()

    user_skills = [
        skill.strip().lower()
        for skill in user_input.split(",")
        if skill.strip()
    ]

    if not user_skills:
        return render_template(
            "index.html",
            error="Please enter at least one skill."
        )

    available_skills = set(
        skill
        for skills in df["skills_list"]
        for skill in skills
    )
    
    invalid_skills = find_invalid_skills(
        user_skills,
        available_skills
    )

    if len(invalid_skills) == len(user_skills):
        return render_template(
            "index.html",
            error="None of the entered skills were found in the dataset."
        )

    filtered_df = filter_internships(
        df.copy(),
        work_mode,
        location
    )
    if filtered_df.empty:
        return render_template(
            "index.html",
            error="No internships found for your selected preferences."
        )

    filtered_df["match_score"] = filtered_df["skills_list"].apply(
        lambda skills: calculate_match(user_skills, skills)
    )

    filtered_df["matched_skills"] = filtered_df["skills_list"].apply(
        lambda skills: get_matched_skills(user_skills, skills)
    )

    filtered_df["missing_skills"] = filtered_df["skills_list"].apply(
        lambda skills: get_missing_skills(user_skills, skills)
    )

    recommendations = get_top_recommendations(filtered_df)

    recommendations = recommendations.reset_index(drop=True)

    return render_template(
        "result.html",
        recommendations=recommendations.to_dict("records")
    )
if __name__ == "__main__":
    app.run(debug=True)
