file_path = "products.txt"

with open(file_path, 'r') as f:
    records = f.readlines()

fp = open("tmp.csv", "a")

cat = "第一批"
for rec in records:
    if "清算后" in rec:
        cat = "清算后"
    if "{" in rec:
        tmp = rec.split("{")
        path = tmp[0]
        products = tmp[-1].split("}")[0].split(",")
        for p in products:
            fp.write(cat+', '+p+', '+path+'\n')

fp.close()