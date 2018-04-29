# Neural Network Programming Assignment 1:

# 問題︰  
  A.the way how you prepare the training samples  
  
    我使用PIL的Image.open()來讀取圖片  
    
  B. all parameters, such as MaxIterLimit, α , and ε , you used for the training algorithm  
  
    MaxIterLimit = 10, α = 1e-5~1e-10,  
    
  C. the derived weight vector w  
  
    w的部份我是使用random來產生隨機亂數，w的數值是介於0-1之間的任一浮點數  
    
  D. the printed image I’ decrypted from E’  
  
    ![error](https://github.com/weiwow123/ML2018_410321114/blob/master/imgResult/decrypted_EP1e-9_10.png)  
    
  E. the problems you encountered  
  
    我一開始遭遇最大的問題是圖片的處理部份，由於之前沒怎麼使用過以pixel對圖片進行修改，所以中間不停出錯。  
    
  F. what you have learned from this work  
  
    我在這份作業中學到如何使用PIL對影像進行簡單的處理，以及如何使用matplotlib建立簡單圖表將資料視覺化。  
    
#討論︰  
  在這次作業中，我將learning rate分別設為1e-5、1e-6、1e-7、1e-8、1e-9、1e-10，看其對結果產生的影響，為了能更好的進行比較，所以將w統一由random改為1e-2，以下是各個Learning Rate的訓練結果︰(以下的epoch皆為10)  
  
![error](https://github.com/weiwow123/ML2018_410321114/blob/master/result/1e-5_10.png)

![error](https://github.com/weiwow123/ML2018_410321114/blob/master/result/1e-6_10.png)

![error](https://github.com/weiwow123/ML2018_410321114/blob/master/result/1e-7_10.png)

![error](https://github.com/weiwow123/ML2018_410321114/blob/master/result/1e-8_10.png)

![error](https://github.com/weiwow123/ML2018_410321114/blob/master/result/1e-9_10.png)

![error](https://github.com/weiwow123/ML2018_410321114/blob/master/result/1e-10_10.png)

由以上的結果可以知道Learing Rate介於1e-5~1e-8之間得出的結果會比較好，另外若是Learning Rate設為1e-10的話，甚至會讓decrypt出來的圖片失敗，以下是用1e-10 decrypt出來的結果︰

![error](https://github.com/weiwow123/ML2018_410321114/blob/master/imgResult_1e-2/decrypted_EP1e-10_10.png)
