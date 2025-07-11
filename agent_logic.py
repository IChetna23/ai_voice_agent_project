import re

def agent_decision(sentiment_label, keywords, transcript_text):
    # Apply reasoning rules to analyze a candidate's transcript based on sentiment, keyword presence, and question handling.

    decision = {
        "tone_issue": False,
        "missing_info": [],
        "candidate_question": False,
        "candidate_questions_list": [],
        "recommended_action": "",
        "Suggested_Response": ""
    }

    # Tone Analysis
    if sentiment_label == "NEGATIVE":
        decision["tone_issue"] = True
        print("Tone Issue Detected: Negative sentiment")

    # Check for missing information
    found_keywords = set(map(str.lower, keywords))
    missing = []

    # Location Check
    if not any(loc in transcript_text.lower() for loc in ["bangalore", "mumbai", "delhi"]):
        missing.append("location")

    # Skills Check
    if not any("python" in kw or "django" in kw for kw in found_keywords):
        missing.append("skills")

    # Experience Check
    if "year" not in transcript_text.lower():
        missing.append("experience")

    if missing:
        decision["missing_info"].extend(missing)
        print("Missing Info Detected:", missing)

    # Detect candidate questions
    questions = re.findall(r'[^.?!]*\?', transcript_text.lower())
    if questions:
        decision["candidate_question"] = True
        decision["candidate_questions_list"] = questions
        print("Candidate Asked Questions:")
        for q in questions:
            print("-", q.strip())

        # Provide response to first relevant question
        q = questions[0]
        if "remote" in q:
            decision["Suggested_Response"] = (
                "Currently we operate in hybrid mode, but we can explore flexibility based on your profile."
            )
        elif "tech" in q or "stack" in q:
            decision["Suggested_Response"] = (
                "You’ll receive the tech stack and detailed job description in a follow-up email."
            )
        elif "role" in q:
            decision["Suggested_Response"] = (
                "This role involves backend development using Python and Django."
            )
        elif "salary" in q:
            decision["Suggested_Response"] = (
                "Salary discussion will happen during the final round."
            )

    # Final decision logic
    if decision["tone_issue"]:
        decision["recommended_action"] = "Flag for HR review"
    elif decision["missing_info"]:
        decision["recommended_action"] = "Prompt candidate for missing info"
    else:
        decision["recommended_action"] = "Proceed to next round"

    return decision