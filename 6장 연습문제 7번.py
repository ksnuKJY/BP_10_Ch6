import turtle

t=turtle.Turtle()
t.shape("turtle")
t.color('blue')
t.lt(90)

for i in range(1,7) :
  t.fd(100)
  t.fd(-30)
  t.lt(60)
  t.fd(30)
  t.fd(-30)

  t.rt(120)
  t.fd(30)
  t.fd(-30)

  t.lt(60)
  t.fd(-70)
  t.lt(60)
