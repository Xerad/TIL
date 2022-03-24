# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Administrator
"""

#%%

# =============================================================================
# =============================================================================
# # 문제 01 유형(DataSet_01.csv 이용)
#
# 구분자 : comma(“,”), 4,572 Rows, 5 Columns, UTF-8 인코딩
# 
# 글로벌 전자제품 제조회사에서 효과적인 마케팅 방법을 찾기
# 위해서 채널별 마케팅 예산과 매출금액과의 관계를 분석하고자
# 한다.
# 컬 럼 / 정 의  /   Type
# TV   /     TV 마케팅 예산 (억원)  /   Double
# Radio / 라디오 마케팅 예산 (억원)  /   Double
# Social_Media / 소셜미디어 마케팅 예산 (억원)  / Double
# Influencer / 인플루언서 마케팅
# (인플루언서의 영향력 크기에 따라 Mega / Macro / Micro / 
# Nano) / String

# SALES / 매출액 / Double
# =============================================================================
# =============================================================================

import pandas as pd
import numpy as np

data1 = pd.read_csv('Dataset_01.csv')
data1.columns
# ['TV', 'Radio', 'Social_Media', 'Influencer', 'Sales']

#%%

# =============================================================================
# 1. 데이터 세트 내에 총 결측값(nan)의 개수는 몇 개인가? (답안 예시) 23
# =============================================================================

# 결측치가 있는 셀의 수
data1.isna().sum().sum()

# 정답: 26

# 결측치가 포함된 행의 수 : 26
data1.isna().any(axis = 1).sum()

# 결측치 관련 함수
#.isna(), .isnull(), .any(), .all(), .dropna(), .fillna()
# np.nan
#%%

# =============================================================================
# 2. TV, Radio, Social Media 등 세 가지 다른 마케팅 채널의 예산과 매출액과의 상관분석을
# 통하여 각 채널이 매출에 어느 정도 연관이 있는지 알아보고자 한다. 
# - 매출액과 가장 강한 상관관계를 가지고 있는 채널의 상관계수를 소수점 5번째
# 자리에서 반올림하여 소수점 넷째 자리까지 기술하시오. (답안 예시) 0.1234
# =============================================================================
var_list = ['TV', 'Radio', 'Social_Media', 'Sales']

q2 = data1[var_list].corr().drop('Sales')['Sales'].abs() # corr() 상관계수 구하는 함수
# q2 = data1[var_list].corr(method=pearson, kendall, spearman)

#q2.min()  최소값
round(q2.max(), 4) # 최대값
# 정답: 0.9995

# [참고]
q2.idxmax() # 최대값의 인덱스명 리턴
q2.argmax() # 최대값이 있는 위치번호 리턴
q2.nlargest(1) # 가장 큰 값(들)이 있는 값과 인덱스명 리턴
q2.nlargest(1).index
q2.rank() # 순위
q2.quantile(0.8) 
q2[q2>0.8].index
#%%

# =============================================================================
# 3. 매출액을 종속변수, TV, Radio, Social Media의 예산을 독립변수로 하여 회귀분석을
# 수행하였을 때, 세 개의 독립변수의 회귀계수를 큰 것에서부터 작은 것 순으로
# 기술하시오. 
# - 분석 시 결측치가 포함된 행은 제거한 후 진행하며, 회귀계수는 소수점 넷째 자리
# 이하는 버리고 소수점 셋째 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================

# from scipy.stats import linregress

from sklearn.linear_model import LinearRegression  # 상수항 포함
from statsmodels.formula.api import ols # 상수항 포함
from statsmodels.api import OLS, add_constant  # 상수항 미포함
# 상수항을 생성(add_constant) 후 회귀진행

# help(data1.corr)
# data1.corr?

### 1. LinearRegression ======================================================

var_list=['TV', 'Radio', 'Social_Media']
q3=data1.dropna()
lm1=LinearRegression(fit_intercept=True)
lm1.fit(q3[var_list],  q3['Sales'])
#[주의]: 결측치 없어야 됨, 입력변수가 2차수

dir(lm1)
lm1.intercept_ # 상수항
lm1.coef_  # 회귀계수

lm1.predict(q3[var_list]) # 예측값 도출
lm1.score(q3[var_list], q3['Sales']) # 결정계수

q3_out1 = pd.Series(lm1.coef_, index = var_list).sort_values(ascending = False)
q3_out1.values
# 정답 :  array([ 3.562,  0.004, -0.003])


### 2. ols(식, 데이터셋).fit() ================================================
# 식: 'y~x1+C(x2)-1'
form1 = 'Sales~TV + Radio + Social_Media'
form1 = 'Sales~' + '+'.join(var_list)

# lm1 = ols(form1, q3)
# lm2 = lm1.fit()

lm2 = ols(form1, q3).fit()
# dir(lm2)_
lm2.summary()

lm2.params[lm2.pvalues < 0.05]

# 이상치 존재하는 경우 해당 데이터 추출
q3[lm2.outlier_test()['bonf(p)'] < 0.05]

q3_out2 = lm2.params.drop('Intercept')
q3_out2.sort_values(ascending = False)
# 정답 :  array([ 3.562,  0.004, -0.003])


# [참고]
form2 = 'Sales~TV-1'
lm3 = ols(form2, q3).fit()
lm3.summary()


# 3. OLS(y, add_constant(x)).fit() ===========================================
lm4 = OLS(q3['Sales'], q3[var_list]).fit()
lm4.summary()

xx = add_constant(q3[var_list])
lm5 = OLS(q3['Sales'], xx).fit()
lm4.summary()

form3 = 'Sales~' + '+'.join(q3.columns.drop('Sales'))

lm6 = ols(form3, q3).fit()
lm6.summary()
# =============================================================================
#%%

# =============================================================================
# =============================================================================
# # 문제 02 유형(DataSet_02.csv 이용)
# 구분자 : comma(“,”), 200 Rows, 6 Columns, UTF-8 인코딩

# 환자의 상태와 그에 따라 처방된 약에 대한 정보를 분석하고자한다
# 
# 컬 럼 / 정 의  / Type
# Age  / 연령 / Integer
# Sex / 성별 / String
# BP / 혈압 레벨 / String
# Cholesterol / 콜레스테롤 레벨 /  String
# Na_to_k / 혈액 내 칼륨에 대비한 나트륨 비율 / Double
# Drug / Drug Type / String
# =============================================================================
# =============================================================================

import numpy as np
import pandas as pd

data2 = pd.read_csv('Dataset_02.csv')
data2.columns


#%%

# =============================================================================
# 1.해당 데이터에 대한 EDA를 수행하고, 여성으로 혈압이 High, Cholesterol이 Normal인
# 환자의 전체에 대비한 비율이 얼마인지 소수점 네 번째 자리에서 반올림하여 소수점 셋째
# 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================



q1 = data2[['Sex', 'BP', 'Cholesterol']].value_counts(normalize = True)

q1.index
q1[('F', 'HIGH', 'NORMAL')]
# 정답 : 0.105


#%%

# =============================================================================
# 2. Age, Sex, BP, Cholesterol 및 Na_to_k 값이 Drug 타입에 영향을 미치는지 확인하기
# 위하여 아래와 같이 데이터를 변환하고 분석을 수행하시오. 
# - Age_gr 컬럼을 만들고, Age가 20 미만은 ‘10’, 20부터 30 미만은 ‘20’, 30부터 40 미만은
# ‘30’, 40부터 50 미만은 ‘40’, 50부터 60 미만은 ‘50’, 60이상은 ‘60’으로 변환하시오. 
# - Na_K_gr 컬럼을 만들고 Na_to_k 값이 10이하는 ‘Lv1’, 20이하는 ‘Lv2’, 30이하는 ‘Lv3’, 30 
# 초과는 ‘Lv4’로 변환하시오.
# - Sex, BP, Cholesterol, Age_gr, Na_K_gr이 Drug 변수와 영향이 있는지 독립성 검정을
# 수행하시오.
# - 검정 수행 결과, Drug 타입과 연관성이 있는 변수는 몇 개인가? 연관성이 있는 변수
# 가운데 가장 큰 p-value를 찾아 소수점 여섯 번째 자리 이하는 버리고 소수점 다섯
# 번째 자리까지 기술하시오.
# (답안 예시) 3, 1.23456
# =============================================================================

# 1. 변수 생성: Age_gr, Na_K_gr
# np.where(조건) 참인 경우의 데이터 위치번호 리턴
# np.where(조건, 참, 거짓) 조건의 결과에 따라 해당하는 값 가져옴.

q2 = data2.copy()
q2['Age_gr'] = np.where(q2.Age < 20, 10, 
                 np.where(q2.Age < 30, 20,
                   np.where(q2.Age < 40, 30,
                     np.where(q2.Age < 50, 40,
                       np.where(q2.Age < 60, 50, 60)))))

q2['Na_K_gr'] = np.where(q2.Na_to_K <= 10, 'Lv1',
                  np.where(q2.Na_to_K <= 20, 'Lv2',
                    np.where(q2.Na_to_K <= 30, 'Lv3', 'Lv4')))

# ============================================================================                     

# 2. Sex, BP, Cholesterol, Age_gr, Na_to_k 값이 Drug 변수와 영향이 있는지 독립성 검정
# (1) 변수별로 독립성 검정 수행하도록 설계
var_list = ['Sex', 'BP', 'Cholesterol', 'Age_gr', 'Na_K_gr']

# (2) 빈도표 작성
tab = pd.crosstab(index = q2['Sex'], columns = q2['Drug'])

# (3) 카이스퀘어 검정 수행
from scipy.stats import chi2_contingency

chi_out = chi2_contingency(tab)
chi_out[1]

# (4) 반복 수행
q2_out = []
for i in var_list:
    tab = pd.crosstab(index = q2[i], columns = q2['Drug'])
    chi_out = chi2_contingency(tab)
    pvalue = chi_out[1]
    q2_out.append([i, pvalue])

q2_out = pd.DataFrame(q2_out, columns = ['var', 'pvalue'])    

# ============================================================================

# 3. Drug 타입과 연관성이 있는 변수는 몇 개인가?
q2_out2 = q2_out[q2_out.pvalue < 0.05]
len(q2_out2)
# 정답: 4

# ============================================================================

# 4. 연관성이 있는 변수 가운데 가장 큰 p-value를 찾아 소수점 여섯 번째 자리 이하는 버리고 
# 소수점 다섯 번째 자리까지 기술하시오. 

q2_out2.pvalue.max() # 0.00070
# 정답 : 0.00070