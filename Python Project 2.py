import pandas as pd

def demographic_data_analyzer():
    # Load the data
    df = pd.read_csv('adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ])

    # 1. Number of each race represented
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degrees
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 4. Percentage with advanced education (Bachelors, Masters, Doctorate) earning >50K
    adv_ed = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    adv_ed_rich = df[adv_ed & (df['salary'] == '>50K')]
    percentage_adv_edu_rich = round(len(adv_ed_rich) / adv_ed.sum() * 100, 1)

    # 5. Percentage without advanced education earning >50K
    non_adv_ed = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    non_adv_ed_rich = df[non_adv_ed & (df['salary'] == '>50K')]
    percentage_non_adv_edu_rich = round(len(non_adv_ed_rich) / non_adv_ed.sum() * 100, 1)

    # 6. Minimum number of hours worked per week
    min_hours = df['hours-per-week'].min()

    # 7. Percentage of people working minimum hours earning >50K
    min_hours_workers = df[df['hours-per-week'] == min_hours]
    rich_min_workers = min_hours_workers[min_hours_workers['salary'] == '>50K']
    percentage_min_hours_rich = round(len(rich_min_workers) / len(min_hours_workers) * 100, 1)

    # 8. Country with highest percentage of >50K earners
    rich_country_table = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_table = df['native-country'].value_counts()
    highest_earning_country = (rich_country_table / country_table * 100).idxmax()
    highest_earning_country_percentage = round((rich_country_table / country_table * 100).max(), 1)

    # 9. Most popular occupation for those earning >50K in India
    rich_indians = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_in_occupation = rich_indians['occupation'].mode() if not rich_indians.empty else None

    # Results dictionary (for convenient testing)
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_adv_edu_rich': percentage_adv_edu_rich,
        'percentage_non_adv_edu_rich': percentage_non_adv_edu_rich,
        'min_hours': min_hours,
        'percentage_min_hours_rich': percentage_min_hours_rich,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_in_occupation': top_in_occupation
    }