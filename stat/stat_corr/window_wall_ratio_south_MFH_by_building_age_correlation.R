# OeQ autogenerated correlation function: Window/Wall Ratio South in Correlation to the Building Age

window_wall_ratio_south_MFH_by_building_age_correlation<-function(...){
# OeQ autogenerated correlation for 'Window to Wall Ratio in Southern Direction'
A_WIN_S_BY_AW = correlation(
    Const = 20818.6194135154,
    a = -42.651351864193,
    b = 0.0327511835634606,
    c = -1.11718058834248e-05,
    d = 1.42836626433628e-09,
    mode="lin")


    return(data.frame(A_WIN_S_BY_AW=lookup(A_WIN_S_BY_AW,...),
    stringsAsFactors=FALSE))
}
