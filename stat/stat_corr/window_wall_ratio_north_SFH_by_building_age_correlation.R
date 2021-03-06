# OeQ autogenerated correlation function: Window/Wall Ratio North in Correlation to the Building Age

window_wall_ratio_north_SFH_by_building_age_correlation<-function(...){
# OeQ autogenerated correlation for 'Window to Wall Ratio in Northern Direction'
A_WIN_N_BY_AW = correlation(
    Const = 12970.3948492661,
    a = -26.6534988175816,
    b = 0.0205282054258593,
    c = -7.02311790303439e-06,
    d = 9.00546817636975e-10,
    mode="lin")


    return(data.frame(A_WIN_N_BY_AW=lookup(A_WIN_N_BY_AW,...),
    stringsAsFactors=FALSE))
}
