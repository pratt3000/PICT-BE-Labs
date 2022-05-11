class ACController:
  def __init__(self):
    self.mapping = self.__get_mappings()
    self.rule_base = self.__get_rules()
    self.td_mf = self.__get_td_mf()
    self.dial_vals = self.__get_dial_vals()
    self.dial_base = self.dial_vals['VH'] - self.dial_vals['MH'] #0.75

  def __get_mappings(self):
    return {
        'VH': 0, # Very Hot
        'HO': 1, # Hot
        'MH': 2, # Mildly Hot
        'BA': 3, # Balanced
        'MC': 4, # Mildly Cold
        'CO': 5, # Cold
        'VC': 6  # Very Cold
    }

  def __get_rules(self):
    return [ 'VC', 'CO', 'MC', 'BA', 'MH', 'HO', 'VH']

  def __get_td_mf(self): # basically defined all he triangles, includng open left and open right
    return {
        'VH': lambda x : 1 if x < -15 else (0 if x > -10 else -0.2*x - 2),
        'HO': lambda x : 0 if x < -15 or x > -5 else (0.2*x + 3 if x < -10 else -0.2*x - 1),
        'MH': lambda x : 0 if x < -10 or x > 0 else (0.2*x + 2 if x < -5 else -0.2*x),
        'BA': lambda x : 0 if abs(x) > 5 else (0.2*x + 1 if x < 0 else -0.2*x + 1),
        'MC': lambda x : 0 if x < 0 or x > 10 else (-0.2*x + 2 if x > 5 else 0.2*x),
        'CO': lambda x : 0 if x < 5 or x > 15 else (-0.2*x + 3 if x < -10 else 0.2*x - 1),
        'VC': lambda x : 1 if x > 15 else (0 if x < 10 else 0.2*x - 2),
    }

  def __get_dial_vals(self):
    return {
        'VC': -1,
        'CO': -0.5,
        'MC': -0.25,
        'BA': 0,
        'MH': 0.25,
        'HO': 0.5,
        'VH': 1     
    }

  def __crisp_to_fuzzy(self, val, mf): # a list is created with [label, its fuzzified value] for all the triangles that get intersected
    fuzzy_values = []
    for x, myu_x in mf.items():
      if myu_x(val) > 0: fuzzy_values.append((x, myu_x(val)))
    return fuzzy_values

  def __fuzzify(self, td):
    return self.__crisp_to_fuzzy(td, self.td_mf)

  def __apply_rule_base(self, td):
    dial_fuzzy = []
    for t in td:
        i = self.mapping[t[0]]
        dial_fuzzy.append((self.rule_base[i], t[1]))
    return dial_fuzzy

  def __get_dial_area(self, x):
    y = self.dial_base * x
    return 0.5 * (self.dial_base - (1 - x) * y)

  def __defuzzify(self, dial_fuzzy):
    areas = []
    for df in dial_fuzzy:
      areas.append((self.dial_vals[df[0]], self.__get_dial_area(df[1])))
    dial = 0
    total_area = 0
    for a in areas:
      dial += a[0] * a[1]
      total_area += a[1]
    return dial / total_area

  def get_dial(self, td):
    td_fuzzy = self.__fuzzify(td)
    dial_fuzzy = self.__apply_rule_base(td_fuzzy)
    dial = self.__defuzzify(dial_fuzzy)
    return dial

controller = ACController()

dial_value = controller.get_dial(td = -20)

print(f'Dial Value: {dial_value}')
