import pandas as pd
import operator

def calculate_demographic_data(print_data=True):
    # Leitura dos dados a partir do arquivo CSV
    df = pd.read_csv('adult.data.csv')

    # Contagem de pessoas de cada raça presente no conjunto de dados
    race_count = df['race'].value_counts()

    # Cálculo da idade média dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentual de pessoas que possuem diploma de Bacharelado
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Filtragem de pessoas com e sem educação avançada (Bacharelado, Mestrado ou Doutorado)
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentual de pessoas com educação avançada que ganham mais de 50K
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)
    
    # Percentual de pessoas sem educação avançada que ganham mais de 50K
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)

    # Número mínimo de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min()

    # Percentual de pessoas que trabalham o mínimo de horas por semana e ganham mais de 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # Identificação do país com a maior porcentagem de pessoas que ganham mais de 50K
    country_groups = df.groupby('native-country')
    rich_country_percentages = (country_groups.apply(lambda x: (x['salary'] == '>50K').mean()) * 100).round(1)
    highest_earning_country = rich_country_percentages.idxmax()
    highest_earning_country_percentage = rich_country_percentages.max()

    # Identificação da ocupação mais comum entre as pessoas que ganham mais de 50K na Índia
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # NÃO MODIFIQUE A PARTE ABAIXO

    if print_data:
        print("Número de cada raça:\n", race_count) 
        print("Idade média dos homens:", average_age_men)
        print(f"Percentual com diploma de Bacharelado: {percentage_bachelors}%")
        print(f"Percentual com ensino superior que ganham >50K: {higher_education_rich}%")
        print(f"Percentual sem ensino superior que ganham >50K: {lower_education_rich}%")
        print(f"Tempo mínimo de trabalho: {min_work_hours} horas/semana")
        print(f"Percentual de ricos entre os que trabalham menos horas: {rich_percentage}%")
        print("País com maior porcentagem de ricos:", highest_earning_country)
        print(f"Maior porcentagem de ricos em um país: {highest_earning_country_percentage}%")
        print("Ocupação mais comum na Índia para quem ganha >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
