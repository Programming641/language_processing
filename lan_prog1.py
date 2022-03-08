from def_human import Human, People
from def_time import Daily_Basis
from def_daily import Everyday_Life

import pickle




people = People()

people.activate("act")
people.activate("think")
people.activate("feel")

people_act_time = Daily_Basis(None, None, in_general=True)

people.set_timespan("act", people_act_time )

people_think_time = Daily_Basis(None, None, in_general=True)

people.set_timespan("think", people_think_time )

people_feel_time = Daily_Basis(None, None, in_general=True)

people.set_timespan("feel", people_feel_time )

def_daily = Everyday_Life()

sentence = "Everyday life, daily life, or routine life comprises the ways in which people typically act, think, and feel on a daily basis."


def_daily.define( sentence , people )



f = open("test.pycldef", mode="wb" )

pickle.dump(people, f)
pickle.dump(def_daily, f)

f.close()






