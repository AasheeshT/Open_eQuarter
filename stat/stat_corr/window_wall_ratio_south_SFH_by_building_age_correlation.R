# OeQ autogenerated correlation function: Window/Wall Ratio South in Correlation to the Building Age

window_wall_ratio_south_SFH_by_building_age_correlation<-function(...){
# OeQ autogenerated correlation for 'Window to Wall Ratio in Southern Direction'
A_WIN_S_BY_AW = correlation(
    Const = 9428.07222626182,
    a = -19.2068359892945,
    b = 0.0146645925133324,
    c = -4.97344110343767e-06,
    d = 6.32178163644181e-10,
    mode="lin")


    return(data.frame(A_WIN_S_BY_AW=lookup(A_WIN_S_BY_AW,...),
    stringsAsFactors=FALSE))
}
