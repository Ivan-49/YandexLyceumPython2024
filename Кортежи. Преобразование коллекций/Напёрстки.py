n_str = int(input())
str_ = [input() for _ in range(n_str)]
n_iter = int(input())

for _ in range(n_iter):
    n_ind = int(input())
    new_str = [str_[int(input()) - 1] for _ in range(n_ind)]    
    str_ = new_str

print(*str_, sep="\n")

