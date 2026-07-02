# Coordinate Geometry (Full Chapter)

Here is the reconstructed text from your PDF extract, presented in a clean, highly readable Markdown format with all mathematical formulas converted to perfect LaTeX.

---

# COORDINATE GEOMETRY
## 7.1 Introduction

In Class IX, you have studied that to locate the position of a point on a plane, we require a pair of coordinate axes. The distance of a point from the y-axis is called its **x-coordinate**, or **abscissa**. The distance of a point from the x-axis is called its **y-coordinate**, or **ordinate**. The coordinates of a point on the x-axis are of the form $(x, 0)$, and of a point on the y-axis are of the form $(0, y)$.

Here is a play for you. Draw a set of a pair of perpendicular axes on a graph paper. Now plot the following points and join them as directed:
Join the point $A(4, 8)$ to $B(3, 9)$ to $C(3, 8)$ to $D(1, 6)$ to $E(1, 5)$ to $F(3, 3)$ to $G(6, 3)$ to $H(8, 5)$ to $I(8, 6)$ to $J(6, 8)$ to $K(6, 9)$ to $L(5, 8)$ to $A$.
Then join the points $P(3.5, 7)$, $Q(3, 6)$ and $R(4, 6)$ to form a triangle.
Also join the points $X(5.5, 7)$, $Y(5, 6)$ and $Z(6, 6)$ to form a triangle.
Now join $S(4, 5)$, $T(4.5, 4)$ and $U(5, 5)$ to form a triangle.
Lastly join $S$ to the points $(0, 5)$ and $(0, 6)$ and join $U$ to the points $(9, 5)$ and $(9, 6)$.
What picture have you got?

Also, you have seen that a linear equation in two variables of the form $ax + by + c = 0$, ($a, b$ are not simultaneously zero), when represented graphically, gives a straight line. Further, in Chapter 2, you have seen the graph of $y = ax^2 + bx + c$ ($a \neq 0$), is a parabola. In fact, coordinate geometry has been developed as an algebraic tool for studying geometry of figures. It helps us to study geometry using algebra, and understand algebra with the help of geometry. Because of this, coordinate geometry is widely applied in various fields such as physics, engineering, navigation, seismology and art!

In this chapter, you will learn how to find the distance between the two points whose coordinates are given. You will also study how to find the coordinates of the point which divides a line segment joining two given points in a given ratio.

## 7.2 Distance Formula

Let us consider the following situation:
A town B is located 36 km east and 15 km north of the town A. How would you find the distance from town A to town B without actually measuring it? Let us see. This situation can be represented graphically as shown in Fig. 7.1. You may use the Pythagoras Theorem to calculate this distance.

---
**Fig. 7.1: Diagram showing town B located 36 km East and 15 km North of town A. It forms a right-angled triangle with the distance AB as the hypotenuse, and the legs being 36 km (East) and 15 km (North).**
---

Now, suppose two points lie on the x-axis. Can we find the distance between them? For instance, consider two points $A(4, 0)$ and $B(6, 0)$ in Fig. 7.2. The points A and B lie on the x-axis. From the figure you can see that $OA = 4$ units and $OB = 6$ units.
Therefore, the distance of B from A, i.e., $AB = OB – OA = 6 – 4 = 2$ units.
So, if two points lie on the x-axis, we can easily find the distance between them.

Now, suppose we take two points lying on the y-axis. Can you find the distance between them? If the points $C(0, 3)$ and $D(0, 8)$ lie on the y-axis, similarly we find that $CD = 8 – 3 = 5$ units (see Fig. 7.2).

Next, can you find the distance of A from C (in Fig. 7.2)? Since $OA = 4$ units and $OC = 3$ units, the distance of A from C, i.e., $AC = \sqrt{3^2 + 4^2} = \sqrt{9+16} = \sqrt{25} = 5$ units. Similarly, you can find the distance of B from D, $BD = \sqrt{6^2 + 8^2} = \sqrt{36+64} = \sqrt{100} = 10$ units.

---
**Fig. 7.2: A Cartesian coordinate system showing points on the x-axis (A(4,0), B(6,0)) and on the y-axis (C(0,3), D(0,8)). The origin O(0,0) is also marked. Lines OA, OB, OC, OD, AC, BD are implied or shown.**
---

Now, if we consider two points not lying on coordinate axis, can we find the distance between them? Yes! We shall use Pythagoras theorem to do so. Let us see an example.

In Fig. 7.3, the points $P(4, 6)$ and $Q(6, 8)$ lie in the first quadrant. How do we use Pythagoras theorem to find the distance between them? Let us draw $PR$ and $QS$ perpendicular to the x-axis from P and Q respectively. Also, draw a perpendicular from P on QS to meet QS at T. Then the coordinates of R and S are $(4, 0)$ and $(6, 0)$, respectively. So, $RS = 6 - 4 = 2$ units. Also, $QS = 8$ units and $TS = PR = 6$ units.

---
**Fig. 7.3: A Cartesian coordinate system with points P(4,6) and Q(6,8) in the first quadrant. Perpendiculars PR and QS are drawn to the x-axis (R is (4,0), S is (6,0)). A perpendicular PT is drawn from P to QS (T is (4,8)). This forms a right-angled triangle PTQ.**
---

Therefore, $QT = QS - TS = 8 - 6 = 2$ units and $PT = RS = 2$ units.
Now, using the Pythagoras theorem in $\triangle PTQ$, we have:
$PQ^2 = PT^2 + QT^2$
$PQ^2 = 2^2 + 2^2 = 4 + 4 = 8$
So, $PQ = \sqrt{8} = 2\sqrt{2}$ units.

How will we find the distance between two points in two different quadrants?
Consider the points $P(6, 4)$ and $Q(–5, –3)$ (see Fig. 7.4). Draw QS perpendicular to the x-axis. Also draw a perpendicular PT from the point P on QS (extended) such that T has the same y-coordinate as P and same x-coordinate as Q, forming a right-angled triangle PTQ.
(A common construction: Draw a line through P parallel to the x-axis, and a line through Q parallel to the y-axis. Let them intersect at T. In this case, T would be $(-5, 4)$.)

---
**Fig. 7.4: A Cartesian coordinate system showing points P(6,4) in the first quadrant and Q(-5,-3) in the third quadrant. A construction is implied where a right-angled triangle PTQ is formed, possibly by drawing a horizontal line through P and a vertical line through Q, meeting at T. This diagram would clearly show PT as the horizontal distance and QT as the vertical distance.**
---

Then $PT = |6 - (-5)| = 11$ units and $QT = |4 - (-3)| = 7$ units. (Why? Because T is at $(-5, 4)$ if you construct it that way. PT is the horizontal distance between $(6,4)$ and $(-5,4)$, and QT is the vertical distance between $(-5,4)$ and $(-5,-3)$).
Using the Pythagoras Theorem to the right triangle PTQ, we get:
$PQ = \sqrt{11^2 + 7^2} = \sqrt{121 + 49} = \sqrt{170}$ units.

Let us now find the distance between any two points $P(x_1, y_1)$ and $Q(x_2, y_2)$. Draw $PR$ and $QS$ perpendicular to the x-axis. A perpendicular from the point P on QS is drawn to meet it at the point T (see Fig. 7.5).

---
**Fig. 7.5: A Cartesian coordinate system showing two generic points P($x_1, y_1$) and Q($x_2, y_2$) in the first quadrant. Perpendiculars PR and QS are drawn from P and Q to the x-axis. A perpendicular PT is drawn from P to QS. This forms a right-angled triangle PTQ, where PT is horizontal and QT is vertical.**
---

Then,
$OR = x_1$, $OS = x_2$.
So, $RS = |x_2 - x_1|$. Since $T$ lies on $QS$, $PT$ is parallel to $RS$.
Therefore, $PT = RS = |x_2 - x_1|$.

Also,
$SQ = y_2$, $ST = PR = y_1$.
So, $QT = |SQ - ST| = |y_2 - y_1|$.

Now, applying the Pythagoras theorem in $\triangle PTQ$, we get:
$PQ^2 = PT^2 + QT^2$
$PQ^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$
Therefore,
$PQ = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$

Note that since distance is always non-negative, we take only the positive square root. So, the distance between the points $P(x_1, y_1)$ and $Q(x_2, y_2)$ is
$$PQ = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
which is called the **distance formula**.

**Remarks:**
1.  In particular, the distance of a point $P(x, y)$ from the origin $O(0, 0)$ is given by $OP = \sqrt{x^2 + y^2}$.
2.  We can also write, $PQ = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$. (Why? Because $(x_2 - x_1)^2 = (x_1 - x_2)^2$ and $(y_2 - y_1)^2 = (y_1 - y_2)^2$ as squaring removes the sign difference.)

---

**Example 1**: Do the points $(3, 2)$, $(–2, –3)$ and $(2, 3)$ form a triangle? If so, name the type of triangle formed.

**Solution**: Let us apply the distance formula to find the distances PQ, QR and PR, where $P(3, 2)$, $Q(–2, –3)$ and $R(2, 3)$ are the given points.
We have:
$PQ = \sqrt{(3 - (-2))^2 + (2 - (-3))^2}$
$PQ = \sqrt{(3 + 2)^2 + (2 + 3)^2}$
$PQ = \sqrt{5^2 + 5^2} = \sqrt{25 + 25} = \sqrt{50}$
$PQ \approx 7.07$ (approx.)

$QR = \sqrt{(-2 - 2)^2 + (-3 - 3)^2}$
$QR = \sqrt{(-4)^2 + (-6)^2}$
$QR = \sqrt{16 + 36} = \sqrt{52}$
$QR \approx 7.21$ (approx.)

$PR = \sqrt{(3 - 2)^2 + (2 - 3)^2}$
$PR = \sqrt{1^2 + (-1)^2}$
$PR = \sqrt{1 + 1} = \sqrt{2}$
$PR \approx 1.41$ (approx.)

To form a triangle, the sum of the lengths of any two sides must be greater than the length of the third side (Triangle Inequality).
1.  $PQ + PR = \sqrt{50} + \sqrt{2} \approx 7.07 + 1.41 = 8.48$. Since $8.48 > \sqrt{52} \approx 7.21$, the condition holds.
2.  $PQ + QR = \sqrt{50} + \sqrt{52} \approx 7.07 + 7.21 = 14.28$. Since $14.28 > \sqrt{2} \approx 1.41$, the condition holds.
3.  $QR + PR = \sqrt{52} + \sqrt{2} \approx 7.21 + 1.41 = 8.62$. Since $8.62 > \sqrt{50} \approx 7.07$, the condition holds.

Since the sum of any two of these distances is greater than the third distance, therefore, the points P, Q and R form a triangle.

To name the type of triangle, let's check the squares of the side lengths:
$PQ^2 = 50$
$QR^2 = 52$
$PR^2 = 2$

Notice that $PQ^2 + PR^2 = 50 + 2 = 52$.
And $QR^2 = 52$.
Since $PQ^2 + PR^2 = QR^2$, by the converse of the Pythagoras theorem, the triangle PQR is a **right-angled triangle**, with the right angle at P.

---

---

Here's the reconstructed text in a clean, readable Markdown format with all mathematical formulas converted to perfect LaTeX:

---

# COORDINATE GEOMETRY

Also, $PQ^2 + PR^2 = QR^2$. By the converse of Pythagoras theorem, we have $\angle P = 90^\circ$.
Therefore, PQR is a right triangle.

---

**Example 2**: Show that the points $(1, 7)$, $(4, 2)$, $(-1, -1)$ and $(-4, 4)$ are the vertices of a square.

**Solution**:
Let $A(1, 7)$, $B(4, 2)$, $C(-1, -1)$ and $D(-4, 4)$ be the given points. One way of showing that $ABCD$ is a square is to use the property that all its sides should be equal and both its diagonals should also be equal. Now,

We calculate the lengths of the sides using the distance formula:
$$
\begin{aligned}
AB &= \sqrt{(1 - 4)^2 + (7 - 2)^2} = \sqrt{(-3)^2 + (5)^2} = \sqrt{9 + 25} = \sqrt{34} \\
BC &= \sqrt{(4 - (-1))^2 + (2 - (-1))^2} = \sqrt{(4 + 1)^2 + (2 + 1)^2} = \sqrt{5^2 + 3^2} = \sqrt{25 + 9} = \sqrt{34} \\
CD &= \sqrt{(-1 - (-4))^2 + (-1 - 4)^2} = \sqrt{(-1 + 4)^2 + (-5)^2} = \sqrt{3^2 + (-5)^2} = \sqrt{9 + 25} = \sqrt{34} \\
DA &= \sqrt{(1 - (-4))^2 + (7 - 4)^2} = \sqrt{(1 + 4)^2 + 3^2} = \sqrt{5^2 + 3^2} = \sqrt{25 + 9} = \sqrt{34}
\end{aligned}
$$
Now, we calculate the lengths of the diagonals:
$$
\begin{aligned}
AC &= \sqrt{(1 - (-1))^2 + (7 - (-1))^2} = \sqrt{(1 + 1)^2 + (7 + 1)^2} = \sqrt{2^2 + 8^2} = \sqrt{4 + 64} = \sqrt{68} \\
BD &= \sqrt{(4 - (-4))^2 + (2 - 4)^2} = \sqrt{(4 + 4)^2 + (-2)^2} = \sqrt{8^2 + (-2)^2} = \sqrt{64 + 4} = \sqrt{68}
\end{aligned}
$$
Since $AB = BC = CD = DA$ and $AC = BD$, all the four sides of the quadrilateral $ABCD$ are equal and its diagonals $AC$ and $BD$ are also equal. Therefore, $ABCD$ is a square.

**Alternative Solution**:
We find the four sides and one diagonal, say, $AC$ as above.
Here $AD^2 + DC^2 = 34 + 34 = 68 = AC^2$. Therefore, by the converse of Pythagoras theorem, $\angle D = 90^\circ$. A quadrilateral with all four sides equal and one angle $90^\circ$ is a square. So, $ABCD$ is a square.

---

**Example 3**: Fig. 7.6 shows the arrangement of desks in a classroom. Ashima, Bharti and Camella are seated at $A(3, 1)$, $B(6, 4)$ and $C(8, 6)$ respectively. Do you think they are seated in a line? Give reasons for your answer.

*Fig. 7.6: This figure depicts a coordinate plane representing a classroom. Points A(3,1), B(6,4), and C(8,6) are marked, suggesting positions of students' desks.*

**Solution**:
Using the distance formula, we have:
$$
\begin{aligned}
AB &= \sqrt{(6 - 3)^2 + (4 - 1)^2} = \sqrt{3^2 + 3^2} = \sqrt{9 + 9} = \sqrt{18} = 3\sqrt{2} \\
BC &= \sqrt{(8 - 6)^2 + (6 - 4)^2} = \sqrt{2^2 + 2^2} = \sqrt{4 + 4} = \sqrt{8} = 2\sqrt{2} \\
AC &= \sqrt{(8 - 3)^2 + (6 - 1)^2} = \sqrt{5^2 + 5^2} = \sqrt{25 + 25} = \sqrt{50} = 5\sqrt{2}
\end{aligned}
$$
Since $AB + BC = 3\sqrt{2} + 2\sqrt{2} = 5\sqrt{2} = AC$, we can say that the points $A$, $B$ and $C$ are collinear. Therefore, they are seated in a line.

---

**Example 4**: Find a relation between $x$ and $y$ such that the point $(x, y)$ is equidistant from the points $(7, 1)$ and $(3, 5)$.

**Solution**:
Let $P(x, y)$ be equidistant from the points $A(7, 1)$ and $B(3, 5)$.
We are given that $AP = BP$. So, $AP^2 = BP^2$.
$$
\begin{aligned}
(x - 7)^2 + (y - 1)^2 &= (x - 3)^2 + (y - 5)^2 \\
x^2 - 14x + 49 + y^2 - 2y + 1 &= x^2 - 6x + 9 + y^2 - 10y + 25 \\
-14x - 2y + 50 &= -6x - 10y + 34 \\
50 - 34 &= -6x + 14x - 10y + 2y \\
16 &= 8x - 8y \\
16 &= 8(x - y) \\
2 &= x - y
\end{aligned}
$$
i.e., $x - y = 2$, which is the required relation.

**Remark**: Note that the graph of the equation $x - y = 2$ is a line. From your earlier studies, you know that a point which is equidistant from A and B lies on the perpendicular bisector of AB. Therefore, the graph of $x - y = 2$ is the perpendicular bisector of AB (see Fig. 7.7).

*Fig. 7.7: This figure shows a coordinate plane with two points A and B, and a line passing between them. This line is the perpendicular bisector of the segment AB, implying that any point on this line is equidistant from A and B.*

---

**Example 5**: Find a point on the y-axis which is equidistant from the points $A(6, 5)$ and $B(-4, 3)$.

**Solution**:
We know that a point on the y-axis is of the form $(0, y)$. So, let the point $P(0, y)$ be equidistant from $A$ and $B$.
Then $AP^2 = BP^2$:
$$
\begin{aligned}
(6 - 0)^2 + (5 - y)^2 &= (-4 - 0)^2 + (3 - y)^2 \\
36 + (25 - 10y + y^2) &= 16 + (9 - 6y + y^2) \\
36 + 25 - 10y + y^2 &= 16 + 9 - 6y + y^2 \\
61 - 10y &= 25 - 6y \\
61 - 25 &= 10y - 6y \\
36 &= 4y \\
y &= 9
\end{aligned}
$$
So, the required point is $(0, 9)$.

Let us check our solution:
$$
\begin{aligned}
AP &= \sqrt{(6 - 0)^2 + (5 - 9)^2} = \sqrt{6^2 + (-4)^2} = \sqrt{36 + 16} = \sqrt{52} \\
BP &= \sqrt{(-4 - 0)^2 + (3 - 9)^2} = \sqrt{(-4)^2 + (-6)^2} = \sqrt{16 + 36} = \sqrt{52}
\end{aligned}
$$
Note: Using the remark above, we see that $(0, 9)$ is the intersection of the y-axis and the perpendicular bisector of AB.

---

## EXERCISE 7.1

1.  Find the distance between the following pairs of points:
    (i) $(2, 3)$, $(4, 1)$
    (ii) $(-5, 7)$, $(-1, 3)$
    (iii) $(a, b)$, $(-a, -b)$

2.  Find the distance between the points $(0, 0)$ and $(36, 15)$. Can you now find the distance between the two towns A and B discussed in Section 7.2?

3.  Determine if the points $(1, 5)$, $(2, 3)$ and $(-2, -11)$ are collinear.

4.  Check whether $(5, -2)$, $(6, 4)$ and $(7, -2)$ are the vertices of an isosceles triangle.

5.  In a classroom, 4 friends are seated at the points A, B, C and D as shown in Fig. 7.8. Champa and Chameli walk into the class and after observing for a few minutes Champa asks Chameli, “Don’t you think ABCD is a square?” Chameli disagrees. Using distance formula, find which of them is correct.

    *Fig. 7.8: This figure illustrates a coordinate grid representing a classroom. Four points, A, B, C, and D, are marked on the grid, forming a quadrilateral. Students Champa and Chameli are observing these seating positions.*

6.  Name the type of quadrilateral formed, if any, by the following points, and give reasons for your answer:
    (i) $(-1, -2)$, $(1, 0)$, $(-1, 2)$, $(-3, 0)$
    (ii) $(-3, 5)$, $(3, 1)$, $(0, 3)$, $(-1, -4)$
    (iii) $(4, 5)$, $(7, 6)$, $(4, 3)$, $(1, 2)$

7.  Find the point on the x-axis which is equidistant from $(2, -5)$ and $(-2, 9)$.

8.  Find the values of $y$ for which the distance between the points $P(2, -3)$ and $Q(10, y)$ is 10 units.

9.  If $Q(0, 1)$ is equidistant from $P(5, -3)$ and $R(x, 6)$, find the values of $x$. Also find the distances $QR$ and $PR$.

10. Find a relation between $x$ and $y$ such that the point $(x, y)$ is equidistant from the point $(3, 6)$ and $(-3, 4)$.

---

## 7.3 Section Formula

Let us recall the situation in Section 7.2. Suppose a telephone company wants to position a relay tower at $P$ between $A$ and $B$ in such a way that the distance of the tower from $B$ is twice its distance from $A$. If $P$ lies on $AB$, it will divide $AB$ in the ratio $1 : 2$ (see Fig. 7.9). If we take $A$ as the origin $O$, and 1 km as one unit on both the axis, the coordinates of $B$ will be $(36, 15)$. In order to know the position of the tower, we must know the coordinates of $P$. How do we find these coordinates?

*Fig. 7.9: This diagram shows a line segment AB in a coordinate plane. Point A is at the origin (0,0), and point B is at (36,15). A point P(x,y) lies on AB such that AP:PB = 1:2. Perpendiculars are drawn from P to the x-axis (meeting at D) and from B to the x-axis (meeting at E). A line segment PC is drawn parallel to the x-axis from P, meeting the vertical line BE at C, forming two similar right-angled triangles $\triangle POD$ and $\triangle BPC$.*

Let the coordinates of $P$ be $(x, y)$. Draw perpendiculars from $P$ and $B$ to the x-axis, meeting it in $D$ and $E$, respectively. Draw $PC$ perpendicular to $BE$. Then, by the AA similarity criterion, studied in Chapter 6, $\triangle POD$ and $\triangle BPC$ are similar.
Therefore,
$$
\frac{OD}{PC} = \frac{OP}{PB} = \frac{1}{2} \quad \text{and} \quad \frac{PD}{BC} = \frac{OP}{PB} = \frac{1}{2}
$$
So, we have the equations:
$$
\frac{x}{36 - x} = \frac{1}{2} \quad \text{and} \quad \frac{y}{15 - y} = \frac{1}{2}
$$
These equations give $x = 12$ and $y = 5$.
You can check that $P(12, 5)$ meets the condition that $OP : PB = 1 : 2$.

Now let us use the understanding that you may have developed through this example to obtain the general formula. Consider any two points $A(x_1, y_1)$ and $B(x_2, y_2)$ and assume that $P(x, y)$ divides $AB$ internally in the ratio $m_1 : m_2$, i.e., $\frac{PA}{PB} = \frac{m_1}{m_2}$ (see Fig. 7.10).

*Fig. 7.10: This figure illustrates the general setup for the section formula. Points A(x1,y1), P(x,y), and B(x2,y2) are collinear. Perpendiculars are drawn from A, P, and B to the x-axis, and parallel lines are drawn from A and P to form similar triangles, allowing for the derivation of the coordinates of P based on the ratio m1:m2.*

---

---

## COORDINATE GEOMETRY

This section focuses on the derivation and application of the Section Formula in coordinate geometry.

### Derivation of the Section Formula

Let's consider a line segment joining the points $A(x_1, y_1)$ and $B(x_2, y_2)$. Let $P(x, y)$ be a point that divides the line segment $AB$ internally in the ratio $m_1 : m_2$.

**Diagram Description:**
Imagine a coordinate plane.
1.  Plot points $A(x_1, y_1)$, $P(x, y)$, and $B(x_2, y_2)$ on a straight line, with P lying between A and B.
2.  Draw perpendiculars from $A$, $P$, and $B$ to the x-axis, meeting it at points $R$, $S$, and $T$ respectively. So, $AR \perp x$-axis, $PS \perp x$-axis, $BT \perp x$-axis.
    *   This means $OR = x_1$, $OS = x$, $OT = x_2$.
    *   Also, $AR = y_1$, $PS = y$, $BT = y_2$.
3.  Draw a line $AQ$ parallel to the x-axis, intersecting $PS$ at $Q$.
4.  Draw a line $PC$ parallel to the x-axis, intersecting $BT$ at $C$.

From the construction, we have two triangles: $\triangle PAQ$ and $\triangle BPC$.
Since $PS \perp x$-axis and $BT \perp x$-axis, $PS \parallel BT$. Also, $AQ \parallel PC$ (both parallel to x-axis).
By the AA similarity criterion (Angle-Angle),
$\triangle PAQ \sim \triangle BPC$

Therefore, the ratio of their corresponding sides must be equal:
$$ \frac{PA}{BP} = \frac{AQ}{PC} = \frac{PQ}{BC} \quad \text{(1)} $$

Now, let's express the lengths of these segments in terms of the coordinates:
*   $AQ = RS = OS - OR = x - x_1$
*   $PC = ST = OT - OS = x_2 - x$
*   $PQ = PS - QS = PS - AR = y - y_1$
*   $BC = BT - CT = BT - PS = y_2 - y$

Since $P$ divides $AB$ in the ratio $m_1 : m_2$, we have $\frac{PA}{BP} = \frac{m_1}{m_2}$.

Substituting these values into equation (1), we get:
$$ \frac{m_1}{m_2} = \frac{x - x_1}{x_2 - x} = \frac{y - y_1}{y_2 - y} $$

**Solving for x-coordinate:**
Taking the first equality:
$$ \frac{m_1}{m_2} = \frac{x - x_1}{x_2 - x} $$
Cross-multiplying:
$$ m_1 (x_2 - x) = m_2 (x - x_1) $$
$$ m_1 x_2 - m_1 x = m_2 x - m_2 x_1 $$
Rearranging to solve for $x$:
$$ m_1 x_2 + m_2 x_1 = m_2 x + m_1 x $$
$$ m_1 x_2 + m_2 x_1 = x (m_1 + m_2) $$
$$ x = \frac{m_1 x_2 + m_2 x_1}{m_1 + m_2} $$

**Solving for y-coordinate:**
Similarly, taking the second equality:
$$ \frac{m_1}{m_2} = \frac{y - y_1}{y_2 - y} $$
Cross-multiplying:
$$ m_1 (y_2 - y) = m_2 (y - y_1) $$
$$ m_1 y_2 - m_1 y = m_2 y - m_2 y_1 $$
Rearranging to solve for $y$:
$$ m_1 y_2 + m_2 y_1 = m_2 y + m_1 y $$
$$ m_1 y_2 + m_2 y_1 = y (m_1 + m_2) $$
$$ y = \frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} $$

So, the coordinates of the point $P(x, y)$ which divides the line segment joining the points $A(x_1, y_1)$ and $B(x_2, y_2)$, internally, in the ratio $m_1 : m_2$ are:
$$ \left( \frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, \frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} \right) \quad \text{(2)} $$
This is known as the **Section Formula**.

**Alternative Derivation:**
This formula can also be derived by drawing perpendiculars from $A$, $P$, and $B$ on the y-axis and proceeding in a similar manner.

**Special Case: Ratio k : 1**
If the ratio in which $P$ divides $AB$ is $k : 1$ (which means $m_1 = k$ and $m_2 = 1$), then the coordinates of the point $P$ will be:
$$ \left( \frac{k x_2 + 1 \cdot x_1}{k + 1}, \frac{k y_2 + 1 \cdot y_1}{k + 1} \right) = \left( \frac{k x_2 + x_1}{k + 1}, \frac{k y_2 + y_1}{k + 1} \right) $$

**Special Case: Mid-point Formula**
The mid-point of a line segment divides the line segment in the ratio $1 : 1$. Therefore, for the mid-point $P$ of the join of the points $A(x_1, y_1)$ and $B(x_2, y_2)$, we take $m_1 = 1$ and $m_2 = 1$.
The coordinates of the mid-point $P$ are:
$$ \left( \frac{1 \cdot x_2 + 1 \cdot x_1}{1 + 1}, \frac{1 \cdot y_2 + 1 \cdot y_1}{1 + 1} \right) = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right) $$

---

### Examples based on the Section Formula

**Example 6:** Find the coordinates of the point which divides the line segment joining the points $(4, -3)$ and $(8, 5)$ in the ratio $3 : 1$ internally.

**Solution:**
Let $P(x, y)$ be the required point. Here, $(x_1, y_1) = (4, -3)$, $(x_2, y_2) = (8, 5)$, $m_1 = 3$, and $m_2 = 1$.
Using the section formula:
$$ x = \frac{m_1 x_2 + m_2 x_1}{m_1 + m_2} = \frac{3(8) + 1(4)}{3 + 1} = \frac{24 + 4}{4} = \frac{28}{4} = 7 $$
$$ y = \frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} = \frac{3(5) + 1(-3)}{3 + 1} = \frac{15 - 3}{4} = \frac{12}{4} = 3 $$
Therefore, the required point is $(7, 3)$.

---

**Example 7:** In what ratio does the point $(-4, 6)$ divide the line segment joining the points $A(-6, 10)$ and $B(3, -8)$?

**Solution:**
Let $(-4, 6)$ divide $AB$ internally in the ratio $m_1 : m_2$.
Here, $(x_1, y_1) = (-6, 10)$, $(x_2, y_2) = (3, -8)$, and $(x, y) = (-4, 6)$.
Using the section formula, we get:
$$ (-4, 6) = \left( \frac{m_1(3) + m_2(-6)}{m_1 + m_2}, \frac{m_1(-8) + m_2(10)}{m_1 + m_2} \right) \quad \text{(1)} $$
Recall that if $(x, y) = (a, b)$ then $x = a$ and $y = b$.
So, we can equate the x-coordinates:
$$ -4 = \frac{3m_1 - 6m_2}{m_1 + m_2} $$
Cross-multiplying:
$$ -4(m_1 + m_2) = 3m_1 - 6m_2 $$
$$ -4m_1 - 4m_2 = 3m_1 - 6m_2 $$
Rearranging the terms:
$$ -4m_1 - 3m_1 = -6m_2 + 4m_2 $$
$$ -7m_1 = -2m_2 $$
$$ 7m_1 = 2m_2 $$
Therefore, the ratio $\frac{m_1}{m_2} = \frac{2}{7}$, or $m_1 : m_2 = 2 : 7$.

**Verification using y-coordinate:**
We should verify that this ratio satisfies the y-coordinate also.
$$ 6 = \frac{-8m_1 + 10m_2}{m_1 + m_2} $$
Substitute $m_1 = 2$ and $m_2 = 7$ (or simply the ratio $\frac{m_1}{m_2} = \frac{2}{7}$, by dividing numerator and denominator by $m_2$):
$$ \frac{-8 \frac{m_1}{m_2} + 10}{\frac{m_1}{m_2} + 1} = \frac{-8 \left(\frac{2}{7}\right) + 10}{\frac{2}{7} + 1} = \frac{-\frac{16}{7} + \frac{70}{7}}{\frac{2+7}{7}} = \frac{\frac{54}{7}}{\frac{9}{7}} = \frac{54}{9} = 6 $$
Since the y-coordinate also matches, our ratio is correct.
Therefore, the point $(-4, 6)$ divides the line segment joining the points $A(-6, 10)$ and $B(3, -8)$ in the ratio $2 : 7$.

**Alternatively:**
The ratio $m_1 : m_2$ can also be written as $k : 1$, where $k = \frac{m_1}{m_2}$. Let $(-4, 6)$ divide $AB$ internally in the ratio $k : 1$.
Using the section formula with ratio $k:1$:
$$ (-4, 6) = \left( \frac{k(3) + 1(-6)}{k+1}, \frac{k(-8) + 1(10)}{k+1} \right) \quad \text{(2)} $$
Equating the x-coordinates:
$$ -4 = \frac{3k - 6}{k+1} $$
$$ -4(k+1) = 3k - 6 $$
$$ -4k - 4 = 3k - 6 $$
$$ -4 + 6 = 3k + 4k $$
$$ 2 = 7k $$
$$ k = \frac{2}{7} $$
So, the ratio $k : 1 = \frac{2}{7} : 1$, which is equivalent to $2 : 7$.
You can check for the y-coordinate also, as shown in the previous method.
Thus, the point $(-4, 6)$ divides the line segment joining the points $A(-6, 10)$ and $B(3, -8)$ in the ratio $2 : 7$.

**Note:** You can also find this ratio by calculating the distances $PA$ and $PB$ and taking their ratios, provided you know that $A$, $P$, and $B$ are collinear.

---

**Example 8:** Find the coordinates of the points of trisection (i.e., points dividing in three equal parts) of the line segment joining the points $A(2, -2)$ and $B(-7, 4)$.

**Solution:**
Let $P$ and $Q$ be the points of trisection of $AB$. This means $AP = PQ = QB$.

**Diagram Description (Fig. 7.11):**
Imagine a line segment $AB$. Point $P$ is located such that it divides $AB$ into $AP$ and $PB$, where $AP = \frac{1}{3} AB$. Point $Q$ is located such that it divides $AB$ into $AQ$ and $QB$, where $AQ = \frac{2}{3} AB$. This implies $AP=PQ=QB$.

1.  **Coordinates of P:**
    Since $AP = PQ = QB$, point $P$ divides $AB$ internally in the ratio $1 : 2$ (because $AP : PB = AP : (PQ+QB) = 1 : (1+1) = 1:2$).
    Here, $(x_1, y_1) = (2, -2)$, $(x_2, y_2) = (-7, 4)$, $m_1 = 1$, and $m_2 = 2$.
    Applying the section formula for $P$:
    $$ P(x, y) = \left( \frac{1(-7) + 2(2)}{1+2}, \frac{1(4) + 2(-2)}{1+2} \right) $$
    $$ P(x, y) = \left( \frac{-7 + 4}{3}, \frac{4 - 4}{3} \right) $$
    $$ P(x, y) = \left( \frac{-3}{3}, \frac{0}{3} \right) $$
    So, the coordinates of $P$ are $(-1, 0)$.

2.  **Coordinates of Q:**
    Point $Q$ divides $AB$ internally in the ratio $2 : 1$ (because $AQ : QB = (AP+PQ) : QB = (1+1) : 1 = 2:1$).
    Here, $(x_1, y_1) = (2, -2)$, $(x_2, y_2) = (-7, 4)$, $m_1 = 2$, and $m_2 = 1$.
    Applying the section formula for $Q$:
    $$ Q(x, y) = \left( \frac{2(-7) + 1(2)}{2+1}, \frac{2(4) + 1(-2)}{2+1} \right) $$
    $$ Q(x, y) = \left( \frac{-14 + 2}{3}, \frac{8 - 2}{3} \right) $$
    $$ Q(x, y) = \left( \frac{-12}{3}, \frac{6}{3} \right) $$
    So, the coordinates of $Q$ are $(-4, 2)$.

Therefore, the coordinates of the points of trisection of the line segment joining $A$ and $B$ are $(-1, 0)$ and $(-4, 2)$.

**Note:** We could also have obtained $Q$ by noting that it is the mid-point of $PB$. Using the mid-point formula for $P(-1,0)$ and $B(-7,4)$:
$Q = \left( \frac{-1 + (-7)}{2}, \frac{0 + 4}{2} \right) = \left( \frac{-8}{2}, \frac{4}{2} \right) = (-4, 2)$. This confirms our result.

---

**Example 9:** Find the ratio in which the y-axis divides the line segment joining the points $(5, -6)$ and $(-1, -4)$. Also find the point of intersection.

**Solution:**
Let the y-axis divide the line segment joining $A(5, -6)$ and $B(-1, -4)$ in the ratio $k : 1$.
Using the section formula, the coordinates of the point of division are:
$$ \left( \frac{k(-1) + 1(5)}{k+1}, \frac{k(-4) + 1(-6)}{k+1} \right) = \left( \frac{-k+5}{k+1}, \frac{-4k-6}{k+1} \right) $$
This point lies on the y-axis. We know that any point on the y-axis has its abscissa (x-coordinate) equal to 0.
Therefore,
$$ \frac{-k+5}{k+1} = 0 $$
$$ -k+5 = 0 $$
$$ k = 5 $$
That is, the ratio is $5 : 1$.

Now, to find the point of intersection, substitute the value of $k = 5$ into the y-coordinate:
$$ y = \frac{-4(5) - 6}{5+1} = \frac{-20 - 6}{6} = \frac{-26}{6} = -\frac{13}{3} $$
So, the point of intersection is $\left( 0, -\frac{13}{3} \right)$.

---

**Example 10:** If the points $A(6, 1)$, $B(8, 2)$, $C(9, 4)$ and $D(p, 3)$ are the vertices of a parallelogram, taken in order, find the value of $p$.

**Solution:**
We know that the diagonals of a parallelogram bisect each other. This means that the mid-point of diagonal $AC$ must be the same as the mid-point of diagonal $BD$.

1.  **Coordinates of the mid-point of AC:**
    Using the mid-point formula for $A(6, 1)$ and $C(9, 4)$:
    $$ \left( \frac{6+9}{2}, \frac{1+4}{2} \right) = \left( \frac{15}{2}, \frac{5}{2} \right) $$

2.  **Coordinates of the mid-point of BD:**
    Using the mid-point formula for $B(8, 2)$ and $D(p, 3)$:
    $$ \left( \frac{8+p}{2}, \frac{2+3}{2} \right) = \left( \frac{8+p}{2}, \frac{5}{2} \right) $$

3.  **Equating the mid-points:**
    Since the mid-points are the same:
    $$ \left( \frac{15}{2}, \frac{5}{2} \right) = \left( \frac{8+p}{2}, \frac{5}{2} \right) $$
    Equating the x-coordinates:
    $$ \frac{15}{2} = \frac{8+p}{2} $$
    $$ 15 = 8+p $$
    $$ p = 15 - 8 $$
    $$ p = 7 $$
The value of $p$ is $7$.

---

Here is the reconstructed text in a clean, highly readable Markdown format with all mathematical formulas converted to perfect LaTeX:

## COORDINATE GEOMETRY

### EXERCISE 7.2

1.  Find the coordinates of the point which divides the join of $(-1, 7)$ and $(4, -3)$ in the ratio $2 : 3$.

2.  Find the coordinates of the points of trisection of the line segment joining $(4, -1)$ and $(-2, -3)$.

3.  To conduct Sports Day activities, in your rectangular shaped school ground ABCD, lines have been drawn with chalk powder at a distance of 1m each. 100 flower pots have been placed at a distance of 1m from each other along AD, as shown in Fig. 7.12. Niharika runs $\frac{1}{4}$th the distance AD on the 2nd line and posts a green flag. Preet runs $\frac{1}{5}$th the distance AD on the eighth line and posts a red flag. What is the distance between both the flags? If Rashmi has to post a blue flag exactly halfway between the line segment joining the two flags, where should she post her flag?

    *(Diagram description for Fig. 7.12: A rectangular school ground ABCD is depicted. Lines are drawn parallel to the side AD, representing 'lanes' at 1m intervals. 100 flower pots are placed along the side AD, also at 1m intervals, suggesting the length of AD is 100m. If we consider AB along the x-axis and AD along the y-axis, the 2nd line corresponds to $x=2$ and the 8th line to $x=8$. Niharika's flag is at $x=2$ and $y = \frac{1}{4} \times 100 = 25$, so coordinates $(2, 25)$. Preet's flag is at $x=8$ and $y = \frac{1}{5} \times 100 = 20$, so coordinates $(8, 20)$.)*

4.  Find the ratio in which the line segment joining the points $(-3, 10)$ and $(6, -8)$ is divided by $(-1, 6)$.

5.  Find the ratio in which the line segment joining $A(1, -5)$ and $B(-4, 5)$ is divided by the $x$-axis. Also find the coordinates of the point of division.

6.  If $(1, 2)$, $(4, y)$, $(x, 6)$ and $(3, 5)$ are the vertices of a parallelogram taken in order, find $x$ and $y$.

7.  Find the coordinates of a point $A$, where $AB$ is the diameter of a circle whose centre is $(2, -3)$ and $B$ is $(1, 4)$.

8.  If $A$ and $B$ are $(-2, -2)$ and $(2, -4)$, respectively, find the coordinates of $P$ such that $AP = \frac{3}{7} AB$ and $P$ lies on the line segment $AB$.

9.  Find the coordinates of the points which divide the line segment joining $A(-2, 2)$ and $B(2, 8)$ into four equal parts.

10. Find the area of a rhombus if its vertices are $(3, 0)$, $(4, 5)$, $(-1, 4)$ and $(-2, -1)$ taken in order. [Hint: Area of a rhombus = $\frac{1}{2}$ (product of its diagonals)]

---

## MATHEMATICS

### 7.4 Summary

In this chapter, you have studied the following points:

1.  The distance between $P(x_1, y_1)$ and $Q(x_2, y_2)$ is $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.

2.  The distance of a point $P(x, y)$ from the origin is $\sqrt{x^2 + y^2}$.

3.  The coordinates of the point $P(x, y)$ which divides the line segment joining the points $A(x_1, y_1)$ and $B(x_2, y_2)$ internally in the ratio $m_1 : m_2$ are
    $$ \left( \frac{m_1 x_2 + m_2 x_1}{m_1 + m_2}, \frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} \right) $$

4.  The mid-point of the line segment joining the points $P(x_1, y_1)$ and $Q(x_2, y_2)$ is
    $$ \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right) $$

### A NOTE TO THE READER

Section 7.3 discusses the Section Formula for the coordinates $(x, y)$ of a point $P$ which divides internally the line segment joining the points $A(x_1, y_1)$ and $B(x_2, y_2)$ in the ratio $m_1 : m_2$ as follows:
$$ x = \frac{m_1 x_2 + m_2 x_1}{m_1 + m_2} $$
$$ y = \frac{m_1 y_2 + m_2 y_1}{m_1 + m_2} $$
Note that, here, $PA : PB = m_1 : m_2$.

However, if $P$ does not lie between $A$ and $B$ but lies on the line $AB$, outside the line segment $AB$, and $PA : PB = m_1 : m_2$, we say that $P$ divides externally the line segment joining the points $A$ and $B$. You will study Section Formula for such case in higher classes.

---

