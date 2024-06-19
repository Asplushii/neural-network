import random

def generate_dataset(num_samples):
    dataset = []
    for _ in range(num_samples):
        age = random.randint(18, 90) 
        income = random.randint(10000, 90000) 
        if age <= 40 and income <= 40000:
            buy_product = 1 
        else:
            buy_product = 0
        dataset.append([age, income, buy_product])
    return dataset

def save_dataset(dataset, filename):
    with open(filename, 'w') as f:
        for data in dataset:
            f.write(f"{data[0]},{data[1]},{data[2]}\n")

dataset = generate_dataset(10000)

save_dataset(dataset, 'product_buying.csv')
