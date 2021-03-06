# OeQ autogenerated correlation function: Age distribution in correlation to average year of construction
source('init.R')
age_distribution_by_average_year_of_construction<-function(...){
# OeQ autogenerated correlation for 'Buildings with housing built before 1919'
BLD_AGE1_BEFORE1919 = correlation(
    Const = 17305.6055113047,
    a = -36.3881499766575,
    b = 0.0287164086005001,
    c = -1.00779128691161e-05,
    d = 1.32677126018113e-09,
    mode="lin")

# OeQ autogenerated correlation for 'Buildings with housing built between 1919 and 1949'
BLD_AGE1_1919TO1949 = correlation(
    Const = 35569.8677831043,
    a = -74.5130920293314,
    b = 0.0584852319918769,
    c = -2.03850586481183e-05,
    d = 2.66224063942606e-09,
    mode="lin")

# OeQ autogenerated correlation for 'Buildings with housing built between 1950 and 1959'
BLD_AGE1_1950TO1959 = correlation(
    Const = 19634.851143036,
    a = -40.3139110208307,
    b = 0.0310158404272475,
    c = -1.05973242330227e-05,
    d = 1.35676404022634e-09,
    mode="lin")

# OeQ autogenerated correlation for 'Buildings with housing built between 1960 and 1969'
BLD_AGE1_1960TO1969 = correlation(
    Const = 1565.83829056543,
    a = -2.45714853732897,
    b = 0.00128442363580707,
    c = -2.23645783329666e-07,
    d = 1565.83829056543,
    mode="lin")

# OeQ autogenerated correlation for 'Buildings with housing built between 1970 and 1979'
BLD_AGE1_1970TO1979 = correlation(
    Const = -13807.4794397319,
    a = 29.4456917825887,
    b = -0.0235344705471605,
    c = 8.35481907329618e-06,
    d = -1.11152868812872e-09,
    mode="lin")

# OeQ autogenerated correlation for 'Buildings with housing built between 1980 and 1989'
BLD_AGE1_1980TO1989 = correlation(
    Const = -30975.4127213721,
    a = 64.4257617572885,
    b = -0.0502414455582571,
    c = 1.74102147726294e-05,
    d = -2.26199334126778e-09,
    mode="lin")

# OeQ autogenerated correlation for 'Buildings with housing built between 1990 and 1999'
BLD_AGE1_1990TO1999 = correlation(
    Const = -78927.6111132575,
    a = 163.688015643643,
    b = -0.127255654658004,
    c = 4.39532475706709e-05,
    d = -5.690715187523e-09,
    mode="lin")

# OeQ autogenerated correlation for 'Buildings with housing built between 2000 and 2005'
BLD_AGE1_2000TO2005 = correlation(
    Const = 11766.6009044599,
    a = -24.6792191619434,
    b = 0.0194109659542562,
    c = -6.78574716302242e-06,
    d = 8.89633599805725e-10,
    mode="lin")

# OeQ autogenerated correlation for 'Buildings with housing built after 2005'
BLD_AGE1_AFTER2006 = correlation(
    Const = 44628.254101757,
    a = -93.1984482031163,
    b = 0.0729744813998099,
    c = -2.53912946008213e-05,
    d = 3.31257598651351e-09,
    mode="lin")


    return(data.frame(BLD_AGE1_BEFORE1919=lookup(BLD_AGE1_BEFORE1919,...),
    BLD_AGE1_1919TO1949=lookup(BLD_AGE1_1919TO1949,...),
    BLD_AGE1_1950TO1959=lookup(BLD_AGE1_1950TO1959,...),
    BLD_AGE1_1960TO1969=lookup(BLD_AGE1_1960TO1969,...),
    BLD_AGE1_1970TO1979=lookup(BLD_AGE1_1970TO1979,...),
    BLD_AGE1_1980TO1989=lookup(BLD_AGE1_1980TO1989,...),
    BLD_AGE1_1990TO1999=lookup(BLD_AGE1_1990TO1999,...),
    BLD_AGE1_2000TO2005=lookup(BLD_AGE1_2000TO2005,...),
    BLD_AGE1_AFTER2006=lookup(BLD_AGE1_AFTER2006,...),
    stringsAsFactors=FALSE))
}
