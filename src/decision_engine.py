def decide_action(result):
    if result["category"] == "Urgent":
        return "FLAG_AND_NOTIFY"
    elif result["category"] == "Newsletter":
        return "ARCHIVE"
    else:
        return "REVIEW_LATER"
