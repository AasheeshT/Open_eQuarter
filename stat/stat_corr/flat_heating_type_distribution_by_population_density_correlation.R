# OeQ autogenerated correlation function: Flat Heating Type Distribution in Correlation to the population density

flat_heating_type_distribution_by_population_density_correlation<-function(...){
# OeQ autogenerated correlation for 'Flats heated by a district heating systems in buildings with housing'
FLT_HEAT_DISTR = correlation(
    Const = -0.0376356597249307,
    a = 0.0556308881230478,
    b = -0.0187745475566966,
    c = 0.00244209863747157,
    d = -7.48369103227172e-05,
    mode="log")

# OeQ autogenerated correlation for 'Flats heated by self-contained central heating systems in buildings with housing'
FLT_HEAT_SCDWELL = correlation(
    Const = -0.0684937601574335,
    a = 0.101280840380474,
    b = -0.0366464845869781,
    c = 0.00535661489888694,
    d = -0.000246366195974467,
    mode="log")

# OeQ autogenerated correlation for 'Flats heated by a block-type combined heat and power plants in buildings with housing'
FLT_HEAT_BLOCKTYPE = correlation(
    Const = 0.00459916148685845,
    a = 1.74044525841747e-05,
    b = -5.43453734006022e-09,
    c = 7.06799781476878e-13,
    mode="lin")

# OeQ autogenerated correlation for 'Flats in buildings with housing heated by a centralheating systems'
FLT_HEAT_CENTRAL = correlation(
    Const = 1.33518852477482,
    a = -0.596050491594902,
    b = 0.211481787231765,
    c = -0.0290821005702667,
    d = 0.00132808255548864,
    mode="log")

# OeQ autogenerated correlation for 'Flats in buildings with housing heated by single room heating systems including stoves and night storage heaters'
FLT_HEAT_SNGLROOM = correlation(
    Const = 0.0606245152716711,
    a = 0.114497071101638,
    b = -0.0432913974939379,
    c = 0.00553116417972235,
    d = -0.000243749816476899,
    mode="log")

# OeQ autogenerated correlation for 'Flats in buildings w/ housing without heating systems'
FLT_HEAT_NONE = correlation(
    Const = -0.0289954397875384,
    a = 0.0447342324728499,
    b = -0.0152803821220934,
    c = 0.00201423156614967,
    d = -9.27184773373012e-05,
    mode="log")


    return(data.frame(FLT_HEAT_DISTR=lookup(FLT_HEAT_DISTR,...),
    FLT_HEAT_SCDWELL=lookup(FLT_HEAT_SCDWELL,...),
    FLT_HEAT_BLOCKTYPE=lookup(FLT_HEAT_BLOCKTYPE,...),
    FLT_HEAT_CENTRAL=lookup(FLT_HEAT_CENTRAL,...),
    FLT_HEAT_SNGLROOM=lookup(FLT_HEAT_SNGLROOM,...),
    FLT_HEAT_NONE=lookup(FLT_HEAT_NONE,...),
    stringsAsFactors=FALSE))
}
