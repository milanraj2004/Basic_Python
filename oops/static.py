class MilanUtils:

    def clean_ingredients(text):
      return [ item.strip() for item in text.split(",")]
    

raw = "water ,Milk,ginger,honey"


# obj = MilanUtils()
# obj.clean_ingredients(raw)

Cleaned = MilanUtils.clean_ingredients(raw)
print(Cleaned)

