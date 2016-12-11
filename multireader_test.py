from mklibpy.file.in_ import MultiReader

__author__ = 'Michael'


def sort(*names):
    with MultiReader(*names) as reader:
        for line_dict in reader:
            print(line_dict)
            val_dict = {}
            min_val = None
            for key in line_dict:
                val = line_dict[key]
                if val is None:
                    continue
                val = int(val)
                val_dict[key] = val
                if min_val is None or min_val > val:
                    min_val = val
            yield min_val
            for key in line_dict:
                if val_dict[key] == min_val:
                    reader.nextline_flags[key] = True
                    break
            for key in line_dict:
                if key not in reader.nextline_flags:
                    reader.nextline_flags[key] = False


print(list(sort("mr1.in", "mr2.in")))
