def calculate_match(user_skills, job_skills):
    matches=0
    for skill in job_skills:
        if skill in user_skills:
            matches+=1
    return ((matches / len(job_skills)) * 100) 

def get_missing_skills(user_skills, job_skills):
    return [skill for skill in job_skills if skill not in user_skills]

def get_matched_skills(user_skills, job_skills):
    return [skill for skill in job_skills if skill in user_skills]

def get_top_recommendations(df, top_n=5):
    recommendations = (
        df.sort_values("match_score", ascending=False)
        .drop_duplicates("job_title")
        .head(top_n)
        .reset_index(drop=True)
    )
    return recommendations

def get_skill_priority(recommendations):
    missing = recommendations["missing_skills"].explode()
    skill_counts = missing.value_counts()
    return skill_counts.head(5)

def filter_internships(df, work_mode, location):
    if work_mode != "any":
        df = df[df["work_mode"].str.lower() == work_mode]

    if location != "any":
        df = df[df["location_city"].str.lower() == location]

    return df

def prepare_internships(df):
    df = df[df["employment_type"] == "Internship"].copy()
    df = df[df["is_active"] == True].copy()
    return df

def display_recommendations(recommendations):
    print("\n========== INTERNSHIP RECOMMENDATIONS ==========\n")

    for i, (_, job) in enumerate(recommendations.iterrows(), start=1):
        print(f"Recommendation {i}")
        print("-" * 45)
        print(f"Job Title        : {job['job_title']}")
        print(f"Category         : {job['job_category']}")
        print(f"Company          : {job['company_name']}")
        print(f"Location         : {job['location_city']}")
        print(f"Work Mode        : {job['work_mode']}")
        print(f"Stipend          : {job['stipend_amount']}")
        print(f"Match Score      : {job['match_score']:.2f}%")
        print(f"Matched Skills   : {', '.join(job['matched_skills'])}")
        print(f"Missing Skills   : {', '.join(job['missing_skills'])}")
        print(f"Application Date : {job['application_deadline']}")
        print()

def find_invalid_skills(user_skills, available_skills):
    return [
        skill
        for skill in user_skills
        if skill not in available_skills
    ]