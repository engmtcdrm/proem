from src.proem import Proem

p = Proem(
    app_nm = 'test-app',
    flavor_text='this is my flavor',
    version='v1.0.0',
    repo_url='https://github.com/test-app',
    repo_issues_url='https://github.com/test-app/issues',
    width=-1
)

print(p.build())

for line in p.build_list():
    print(line)
