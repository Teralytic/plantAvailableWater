def soilTex(soilTexture):
    if soilTexture == 'Sand':
        FC = 13.7 
        PWP = 6.5
        MPAW = FC - PWP
        coef = 1
    elif soilTexture == 'Fine sand':
        FC = 13.7
        PWP = 6.5
        MPAW = FC - PWP
        coef = 4.5
    elif soilTexture == 'Very fine sand':
        FC = 13.7
        PWP = 6.5
        MPAW = FC - PWP
        coef = 4.5
    elif soilTexture == 'Coarse sand':
        FC = 13.7
        PWP = 10.2
        MPAW = FC - PWP
        coef = 1
    elif soilTexture == 'Loamy sand':
        FC = 14.0
        PWP = 5.0
        MPAW = FC - PWP
        coef = 4
    elif soilTexture == 'Loamy very fine sand':
        FC = 14.0
        PWP = 5.0
        MPAW = FC - PWP 
        coef = 5.5
    elif soilTexture == 'Loamy coarse sand':
        FC = 14.0
        PWP = 5.0
        MPAW = FC - PWP 
        coef = 4
    elif soilTexture == 'Sandy loam':
        FC = 20.0
        PWP = 7.5
        MPAW = FC - PWP
        coef = 4.3
    elif soilTexture == 'Fine sandy loam':
        FC = 20.0
        PWP = 4.0
        MPAW = FC - PWP
        coef = 3.3
    elif soilTexture == 'Very fine sandy loam':
        FC = 23.0
        PWP = 5.0 
        MPAW = FC - PWP
        coef = 3.7
    elif soilTexture == 'Loamy fine sand':
        FC = 13.7
        PWP = 6.5 
        MPAW = FC - PWP
        coef = 8.65
    elif soilTexture == 'Coarse sandy loam':
        FC = 30.3
        PWP = 17.8 
        MPAW = FC - PWP 
        coef = 4.53
    elif soilTexture == 'Loam':
        FC = 30.3
        PWP = 12.3
        MPAW = FC - PWP
        coef = 3.42
    elif soilTexture == 'Silt loam':
        FC = 33.3
        PWP = 12.4 
        MPAW = FC - PWP
        coef = 3
    elif soilTexture == 'Silt':
        FC = 29.5
        PWP = 12.0 
        MPAW = FC - PWP
        ceof = 3.6
    elif soilTexture == 'Sandy clay loam':
        FC = 31.5
        PWP = 15.3 
        MPAW = FC - PWP
        coef = 3.68
    elif soilTexture == 'Clay loam':
        FC = 35.7
        PWP = 19.3 
        MPAW = FC - PWP
        coef = 4.92
    elif soilTexture == 'Silty clay loam':
        FC = 37.0 
        PWP = 18.3
        MPAW = FC - PWP
        coef = 3.72
    elif soilTexture == 'Sandy clay':
        FC = 28.0
        PWP = 16.0
        MPAW = FC - PWP
        coef = 6.8
    elif soilTexture == 'Silty clay':
        FC = 40.0 
        PWP = 22.5
        MPAW = FC - PWP
        coef = 3.5
    elif soilTexture == 'Clay':
        FC = 40.3 
        PWP = 26.0
        MPAW = FC - PWP
        coef = 5.2
    else:
        FC = 30.3
        PWP = 12.3
        MPAW = FC - PWP
        coef = 3.42
        
    return [FC,PWP,MPAW,coef]