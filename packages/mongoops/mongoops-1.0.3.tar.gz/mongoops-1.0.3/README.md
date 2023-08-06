# mongoops - eleka12

This package built on top of pymongo to make ease of using MongoDB atlas operations.

# How to use -

* install the latest package 

> * in jupyter notebook -
```
    !pip install mongoops
```

> * in command prompt -
```bash    
    pip install mongoops
```

* Now run below snippets of code in your jupyter-notebooks / python project to use pytorch defined functions

## Import mongoops

```python

from mongoops.ops import MongoDBOperation

```

## Use your MongoDB atlas Database username / Password and atlas URL

```python

USERNAME = " "

PASSWORD = " "

URL = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.ornbe.mongodb.net/test"

```



## pypi repo link -

[mongoops](https://pypi.org/project/mongoops/)



