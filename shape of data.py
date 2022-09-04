from cmath import sqrt
 

from mean_median_mode_variance_range import mean_meadian_mode, quartile

def skewness(dat):
    q=quartile(dat,'3')
    a=sqrt(q)
    print(f"Standard deviation is : {a}")
    mean_d=mean_meadian_mode(dat,'1')
    print(f"Mean of the data is : {mean_d}")
    median_d=mean_meadian_mode(dat,'3')
    print(f"Median of the data is : {median_d}")
    skew=(3*(mean_d-median_d))/a
    print(f"Skewness is : {skew}")
    if (skew<=complex(0.5) and skew>=complex(-0.5)):
        print(f"Data is a Symmetrical ( Bell Shaped Data ) {skew}")
    elif skew>=0.5 and skew<=1:
        print(f"Data is  Moderatley Positively Skewed by {skew} ")
    elif skew>=-1.0 and skew<=-0.5:
        print(f"Data is Moderately Negative Skewed by {skew}")
    elif skew>=1:
        print(f"Data is Highly Positively Skewed by {skew}")
    elif skew>=-1:
        print(f'Data is Highly Negatively Skewed by {skew}')






x=list(map(int,input("Enter a list ").split()))

print(skewness(x))