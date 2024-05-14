def solution(today, terms, privacies):
    answer = []

    terms_dict = {}
    for i in terms:
        key, value = i.split()
        terms_dict[key] = value

    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        privacy_year, privacy_month, privacy_day = map(int, date.split('.'))
        today_year, today_month, today_day = map(int, today.split('.'))
        expiration_date = (privacy_year - today_year) * 12 * 28 + (privacy_month -
                                                                   today_month) * 28 + (privacy_day - today_day) + terms_dict[term] * 28
        if expiration_date < 0:
            answer.append(i + 1)

    return answer
