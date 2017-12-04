'''Mudit Kapoor 10352635'''
num2 <- 1

add <- function(x, y) {
  return(x + y)
}

subtract <- function(x, y) {
  return(x - y)
}

multiply <- function(x, y) {
  return(x * y)
}

divide <- function(x, y) {
  if (num2 == 0)
    return
  else
    return(x / y)
}

power <- function(x, y) {
  return(x^y)
}

sqrts <-function(x) {
  return (sqrt(x))
}


exp <- function(x, y) {
  return(x ** y)
}

sine <- function(x) {
  return(sin(x))
}

coS <- function(x) {
  return(cos(x))
}

taN <- function(x) {
  return(tan(x))
}


print("Make Selection for calculation")
print("a.AUTOMATIC CALCULATIONS")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Exponential")
print("7.Square Root")
print("8.Sin")
print("9.Cos")
print("10.Tan")
print("q.Quit")

loop <- TRUE
while(loop){
  intselected = c()
 
  selection = readline(prompt="Enter your selection: ")
  
  selected = tolower(selection)
  if (selected == "q") {
    print("Goodbye")
    break()
  }
  
  if (selected == "a") {
    print(paste("45 plus 45 = ",add(45,45)))
    print(paste("45 minus 15 = ",subtract(45,15)))
    print(paste("3 times 15 = ",multiply(3,15)))
    print(paste("45 divided by 15 = ",divide(45,15)))
    print(paste("3 to power of 3 = ",power(3,3)))
    print(paste("3 exponentiate 3 = ",exp(3,3)))
    print(paste("Square root of 36 = ",sqrts(36)))
    print(paste("Sin 45 = ",sine(45)))
    print(paste("Cos 45 = ",coS(45)))
    print(paste("Tan 45 = ",taN(45)))
    print("Goodbye!")
    break()
  }
  
  intselected = as.integer(selected)
  
  if (intselected < 0 || intselected > 10){
    print("You have made an invalid selection, Goodbye!")
    break()
  }
 
  num1 = as.numeric(readline(prompt="Enter number for calculation: "))
  
  if (intselected <=6) {
    num2 = as.numeric(readline(prompt="Enter second number: "))
  }

  operator <- switch(intselected,"Plus","Minus","Times","Divided by","To the Power of", "to Exponent of","The Square Root of","Sin of","Cos of","Tan of")
 
  result <- switch(intselected, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2)
                   ,power(num1, num2), exp(num1, num2), sqrts(num1), sine(num1), coS(num1), taN(num1))
  
  if (intselected <=6){
    print(paste(num1, operator, num2, "=", result))
  } else print(paste( operator, num1, "=", result))
  
  ask = readline(prompt="Do you wish to do another calculation? Type y or any other key >")
  if (ask != "y" )
    loop <- FALSE
  print("Goodbye!")
}