def make_chai():
    if not kettle_has_water():
        fill_kettle()
    plug_in_water()
    boil_water()
    
    if not is_cup_clean():
        wash_up()
    add_up_cup("tea_leaves")
    add_up_cup("Sugar")
    pour("boiled water")
    stil("cup")
    serve("chai")
    
make_chai()