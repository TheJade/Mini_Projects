#PROGRAM that converts a copied and pasted list of words and stuff to #a more useable form so I can use a large list of words for a hangman
#game   
#coded by Jade FjestaD


string = '''		people	372		(noun)
history	187		(noun)
way	185		(noun)
art	183		(noun)
world	169		(noun)
information	168		(noun)
map	167		(noun)
two	164		(noun)
family	159		(noun)
government	143		(noun)
health	122		(noun)
system	111		(noun)
computer	109		(noun)
meat	99		(noun)
year	96		(noun)
thanks	84		(noun)
music	80		(noun)
person	80		(noun)
reading	77		(noun)
method	76		(noun)
data	74		(noun)
food	73		(noun)
understanding	73		(noun)
theory	71		(noun)
law	70		(noun)
bird	68		(noun)
literature	67		(noun)
problem	66		(noun)
software	63		(noun)
control	62		(noun)
knowledge	62		(noun)
power	62		(noun)
ability	61		(noun)
economics	61		(noun)
love	60		(noun)
internet	59		(noun)
television	59		(noun)
science	58		(noun)
library	57		(noun)
nature	57		(noun)
fact	56		(noun)
product	56		(noun)
idea	55		(noun)
temperature	55		(noun)
investment	52		(noun)
area	50		(noun)
society	50		(noun)
activity	48		(noun)
story	48		(noun)
industry	47		(noun)
media	47		(noun)
thing	47		(noun)
oven	45		(noun)
community	44		(noun)
definition	44		(noun)
safety	44		(noun)
quality	43		(noun)
development	42		(noun)
language	42		(noun)
management	41		(noun)
player	41		(noun)
variety	41		(noun)
video	41		(noun)
week	41		(noun)
security	38		(noun)
country	37		(noun)
exam	37		(noun)
movie	37		(noun)
organization	37		(noun)
equipment	35		(noun)
physics	35		(noun)
analysis	34		(noun)
policy	34		(noun)
series	34		(noun)
thought	34		(noun)
basis	33		(noun)
boyfriend	33		(noun)
direction	33		(noun)
strategy	33		(noun)
technology	33		(noun)
army	32		(noun)
camera	32		(noun)
freedom	32		(noun)
paper	32		(noun)
environment	31		(noun)
child	30		(noun)
instance	30		(noun)
month	30		(noun)
truth	30		(noun)
marketing	29		(noun)
university	29		(noun)
writing	29		(noun)
article	28		(noun)
department	28		(noun)
difference	28		(noun)
goal	28		(noun)
news	28		(noun)
audience	27		(noun)
fishing	27		(noun)
growth	27		(noun)
income	27		(noun)
marriage	27		(noun)
user	27		(noun)
combination	26		(noun)
failure	26		(noun)
meaning	26		(noun)
medicine	26		(noun)
philosophy	26		(noun)
teacher	25		(noun)
communication	24		(noun)
night	24		(noun)
chemistry	23		(noun)
disease	23		(noun)
disk	23		(noun)
energy	23		(noun)
nation	23		(noun)
road	23		(noun)
role	23		(noun)
soup	23		(noun)
advertising	22		(noun)
location	22		(noun)
success	22		(noun)
addition	21		(noun)
apartment	21		(noun)
education	21		(noun)
math	21		(noun)
moment	21		(noun)
painting	21		(noun)
politics	21		(noun)
attention	20		(noun)
decision	20		(noun)
event	20		(noun)
property	20		(noun)
shopping	20		(noun)
student	20		(noun)
wood	20		(noun)
competition	19		(noun)
distribution	19		(noun)
entertainment	19		(noun)
office	19		(noun)
population	19		(noun)
president	19		(noun)
unit	19		(noun)
category	18		(noun)
cigarette	18		(noun)
context	18		(noun)
introduction	18		(noun)
opportunity	18		(noun)
performance	18		(noun)
driver	17		(noun)
flight	17		(noun)
length	17		(noun)
magazine	17		(noun)
newspaper	17		(noun)
relationship	17		(noun)
teaching	17		(noun)
cell	16		(noun)
dealer	16		(noun)
finding	16		(noun)
lake	16		(noun)
member	16		(noun)
message	16		(noun)
phone	16		(noun)
scene	16		(noun)
appearance	15		(noun)
association	15		(noun)
concept	15		(noun)
customer	15		(noun)
death	15		(noun)
discussion	15		(noun)
housing	15		(noun)
inflation	15		(noun)
insurance	15		(noun)
mood	15		(noun)
woman	15		(noun)
advice	14		(noun)
blood	14		(noun)
effort	14		(noun)
expression	14		(noun)
importance	14		(noun)
opinion	14		(noun)
payment	14		(noun)
reality	14		(noun)
responsibility	14		(noun)
situation	14		(noun)
skill	14		(noun)
statement	14		(noun)
wealth	14		(noun)
application	13		(noun)
city	13		(noun)
county	13		(noun)
depth	13		(noun)
estate	13		(noun)
foundation	13		(noun)
grandmother	13		(noun)
heart	13		(noun)
perspective	13		(noun)
photo	13		(noun)
recipe	13		(noun)
studio	13		(noun)
topic	13		(noun)
collection	12		(noun)
depression	12		(noun)
imagination	12		(noun)
passion	12		(noun)
percentage	12		(noun)
resource	12		(noun)
setting	12		(noun)
ad	11		(noun)
agency	11		(noun)
college	11		(noun)
connection	11		(noun)
criticism	11		(noun)
debt	11		(noun)
description	11		(noun)
memory	11		(noun)
patience	11		(noun)
secretary	11		(noun)
solution	11		(noun)
administration	10		(noun)
aspect	10		(noun)
attitude	10		(noun)
director	10		(noun)
personality	10		(noun)
psychology	10		(noun)
recommendation	10		(noun)
response	10		(noun)
selection	10		(noun)
storage	10		(noun)
version	10		(noun)
alcohol	9		(noun)
argument	9		(noun)
complaint	9		(noun)
contract	9		(noun)
emphasis	9		(noun)
highway	9		(noun)
loss	9		(noun)
membership	9		(noun)
possession	9		(noun)
preparation	9		(noun)
steak	9		(noun)
union	9		(noun)
agreement	8		(noun)
cancer	8		(noun)
currency	8		(noun)
employment	8		(noun)
engineering	8		(noun)
entry	8		(noun)
interaction	8		(noun)
mixture	8		(noun)
preference	8		(noun)
region	8		(noun)
republic	8		(noun)
tradition	8		(noun)
virus	8		(noun)
actor	7		(noun)
classroom	7		(noun)
delivery	7		(noun)
device	7		(noun)
difficulty	7		(noun)
drama	7		(noun)
election	7		(noun)
engine	7		(noun)
football	7		(noun)
guidance	7		(noun)
hotel	7		(noun)
owner	7		(noun)
priority	7		(noun)
protection	7		(noun)
suggestion	7		(noun)
tension	7		(noun)
variation	7		(noun)
anxiety	6		(noun)
atmosphere	6		(noun)
awareness	6		(noun)
bath	6		(noun)
bread	6		(noun)
candidate	6		(noun)
climate	6		(noun)
comparison	6		(noun)
confusion	6		(noun)
construction	6		(noun)
elevator	6		(noun)
emotion	6		(noun)
employee	6		(noun)
employer	6		(noun)
guest	6		(noun)
height	6		(noun)
leadership	6		(noun)
mall	6		(noun)
manager	6		(noun)
operation	6		(noun)
recording	6		(noun)
sample	6		(noun)
transportation	6		(noun)
charity	5		(noun)
cousin	5		(noun)
disaster	5		(noun)
editor	5		(noun)
efficiency	5		(noun)
excitement	5		(noun)
extent	5		(noun)
feedback	5		(noun)
guitar	5		(noun)
homework	5		(noun)
leader	5		(noun)
mom	5		(noun)
outcome	5		(noun)
permission	5		(noun)
presentation	5		(noun)
promotion	5		(noun)
reflection	5		(noun)
refrigerator	5		(noun)
resolution	5		(noun)
revenue	5		(noun)
session	5		(noun)
singer	5		(noun)
tennis	5		(noun)
basket	4		(noun)
bonus	4		(noun)
cabinet	4		(noun)
childhood	4		(noun)
church	4		(noun)
clothes	4		(noun)
coffee	4		(noun)
dinner	4		(noun)
drawing	4		(noun)
hair	4		(noun)
hearing	4		(noun)
initiative	4		(noun)
judgment	4		(noun)
lab	4		(noun)
measurement	4		(noun)
mode	4		(noun)
mud	4		(noun)
orange	4		(noun)
poetry	4		(noun)
police	4		(noun)
possibility	4		(noun)
procedure	4		(noun)
queen	4		(noun)
ratio	4		(noun)
relation	4		(noun)
restaurant	4		(noun)
satisfaction	4		(noun)
sector	4		(noun)
signature	4		(noun)
significance	4		(noun)
song	4		(noun)
tooth	4		(noun)
town	4		(noun)
vehicle	4		(noun)
volume	4		(noun)
wife	4		(noun)
accident	3		(noun)
airport	3		(noun)
appointment	3		(noun)
arrival	3		(noun)
assumption	3		(noun)
baseball	3		(noun)
chapter	3		(noun)
committee	3		(noun)
conversation	3		(noun)
database	3		(noun)
enthusiasm	3		(noun)
error	3		(noun)
explanation	3		(noun)
farmer	3		(noun)
gate	3		(noun)
girl	3		(noun)
hall	3		(noun)
historian	3		(noun)
hospital	3		(noun)
injury	3		(noun)
instruction	3		(noun)
maintenance	3		(noun)
manufacturer	3		(noun)
meal	3		(noun)
perception	3		(noun)
pie	3		(noun)
poem	3		(noun)
presence	3		(noun)
proposal	3		(noun)
reception	3		(noun)
replacement	3		(noun)
revolution	3		(noun)
river	3		(noun)
son	3		(noun)
speech	3		(noun)
tea	3		(noun)
village	3		(noun)
warning	3		(noun)
winner	3		(noun)
worker	3		(noun)
writer	3		(noun)
assistance	2		(noun)
breath	2		(noun)
buyer	2		(noun)
chest	2		(noun)
chocolate	2		(noun)
conclusion	2		(noun)
contribution	2		(noun)
cookie	2		(noun)
courage	2		(noun)
dad	2		(noun)
desk	2		(noun)
drawer	2		(noun)
establishment	2		(noun)
examination	2		(noun)
garbage	2		(noun)
grocery	2		(noun)
honey	2		(noun)
impression	2		(noun)
improvement	2		(noun)
independence	2		(noun)
insect	2		(noun)
inspection	2		(noun)
inspector	2		(noun)
king	2		(noun)
ladder	2		(noun)
menu	2		(noun)
penalty	2		(noun)
piano	2		(noun)
potato	2		(noun)
profession	2		(noun)
professor	2		(noun)
quantity	2		(noun)
reaction	2		(noun)
requirement	2		(noun)
salad	2		(noun)
sister	2		(noun)
supermarket	2		(noun)
tongue	2		(noun)
weakness	2		(noun)
wedding	2		(noun)
affair	1		(noun)
ambition	1		(noun)
analyst	1		(noun)
apple	1		(noun)
assignment	1		(noun)
assistant	1		(noun)
bathroom	1		(noun)
bedroom	1		(noun)
beer	1		(noun)
birthday	1		(noun)
celebration	1		(noun)
championship	1		(noun)
cheek	1		(noun)
client	1		(noun)
consequence	1		(noun)
departure	1		(noun)
diamond	1		(noun)
dirt	1		(noun)
ear	1		(noun)
fortune	1		(noun)
friendship	1		(noun)
funeral	1		(noun)
gene	1		(noun)
girlfriend	1		(noun)
hat	1		(noun)
indication	1		(noun)
intention	1		(noun)
lady	1		(noun)
midnight	1		(noun)
negotiation	1		(noun)
obligation	1		(noun)
passenger	1		(noun)
pizza	1		(noun)
platform	1		(noun)
poet	1		(noun)
pollution	1		(noun)
recognition	1		(noun)
reputation	1		(noun)
shirt	1		(noun)
sir	1		(noun)
speaker	1		(noun)
stranger	1		(noun)
surgery	1		(noun)
sympathy	1		(noun)
tale	1		(noun)
throat	1		(noun)
trainer	1		(noun)
uncle	1		(noun)
youth	1		(noun)
time	369		(noun, adjective, verb)
work	224		(noun, adjective, verb)
film	209		(noun, verb)
water	201		(noun, verb, adjective)
money	174		(noun, adjective)
example	147		(noun, verb)
while	147		(noun, conjunction, preposition)
business	127		(noun, adjective)
study	118		(noun, verb)
game	117		(noun, adjective, verb)
life	107		(noun, adjective)
form	99		(noun, verb)
air	98		(noun, verb)
day	98		(noun, adjective)
place	98		(noun, verb)
number	97		(noun, verb)
part	96		(noun, verb, adverb)
field	95		(noun, verb, adjective)
fish	92		(noun, verb)
back	86		(noun, adverb, verb)
process	85		(noun, verb)
heat	84		(noun, verb)
hand	81		(noun, verb)
experience	80		(noun, verb)
job	80		(noun, verb)
book	77		(noun, verb)
end	76		(noun, verb)
point	74		(noun, verb)
type	74		(noun, verb)
home	72		(noun, adjective, adverb)
economy	71		(noun, adjective)
value	70		(noun, verb)
body	69		(noun, verb)
market	69		(noun, verb)
guide	68		(noun, verb)
interest	67		(noun, verb)
state	63		(noun, verb)
radio	62		(noun, verb)
course	61		(noun, verb)
company	60		(noun, verb)
price	60		(noun, verb)
size	60		(noun, verb, adjective)
card	58		(noun, verb)
list	58		(noun, verb)
mind	58		(noun, verb)
trade	58		(noun, verb)
line	56		(noun, verb)
care	55		(noun, verb)
group	55		(noun, verb)
risk	55		(noun, verb)
word	55		(noun, verb, interjection)
fat	54		(noun, adjective, verb)
force	54		(noun, verb)
key	54		(noun, adjective, verb)
light	54		(noun, verb, adjective)
training	54		(noun, adjective)
name	53		(noun, verb, adjective)
school	53		(noun, verb)
top	53		(noun, adjective, verb)
amount	51		(noun, verb)
level	51		(noun, adjective, verb)
order	51		(noun, verb)
practice	51		(noun, verb)
research	51		(noun, verb)
sense	51		(noun, verb)
service	51		(noun, verb)
piece	50		(noun, verb)
web	49		(noun, verb)
boss	48		(noun, verb, adjective)
sport	47		(noun, verb)
fun	46		(noun, adjective, verb)
house	46		(noun, adjective, verb)
page	46		(noun, verb)
term	46		(noun, verb)
test	46		(noun, verb)
answer	45		(noun, verb)
sound	45		(noun, verb, adjective)
focus	44		(noun, verb)
matter	44		(noun, verb)
kind	43		(noun, adjective)
soil	43		(noun, verb)
board	42		(noun, verb)
oil	42		(noun, verb)
picture	42		(noun, verb)
access	41		(noun, verb, adjective)
garden	41		(noun, verb)
range	41		(noun, verb)
rate	41		(noun, verb)
reason	41		(noun, verb)
future	40		(noun, adjective)
site	40		(noun, verb)
demand	39		(noun, verb)
exercise	39		(noun, verb)
image	39		(noun, verb)
case	38		(noun, verb)
cause	38		(noun, verb)
coast	38		(noun, verb)
action	37		(noun, adjective)
age	37		(noun, verb)
bad	37		(noun, adverb, adjective)
boat	37		(noun, verb)
record	37		(noun, verb)
result	37		(noun, verb)
section	37		(noun, verb)
building	36		(noun, verb)
mouse	36		(noun, verb)
cash	35		(noun, verb)
class	35		(noun, verb, adjective)
nothing	35		(noun, pronoun, adjective)
period	35		(noun, adjective)
plan	35		(noun, verb)
store	35		(noun, verb)
tax	35		(noun, verb)
side	34		(noun, verb)
subject	34		(noun, adjective, adverb)
space	33		(noun, verb)
rule	32		(noun, verb)
stock	32		(noun, adjective, verb)
weather	32		(noun, verb)
chance	31		(noun, adjective, verb)
figure	31		(noun, verb)
man	31		(noun, verb, interjection)
model	31		(noun, verb)
source	31		(noun, verb)
beginning	30		(noun, adjective, verb)
earth	30		(noun, verb)
program	30		(noun, verb)
chicken	29		(noun, adjective)
design	29		(noun, verb)
feature	29		(noun, verb)
head	29		(noun, adjective, verb)
material	29		(noun, adjective)
purpose	29		(noun, verb)
question	29		(noun, verb)
rock	29		(noun, verb)
salt	29		(noun, adjective, verb)
act	28		(noun, verb)
birth	28		(noun, verb)
car	28		(noun, adjective)
dog	28		(noun, verb)
object	28		(noun, verb)
scale	28		(noun, verb)
sun	28		(noun, verb)
note	27		(noun, verb)
profit	27		(noun, verb)
rent	27		(noun, verb)
speed	27		(noun, verb)
style	27		(noun, verb)
war	27		(noun, verb)
bank	26		(noun, verb)
craft	26		(noun, verb)
half	26		(noun, predeterminer, adverb)
inside	26		(noun, adjective, preposition)
outside	26		(noun, adjective, preposition)
standard	26		(noun, adjective)
bus	25		(noun, verb)
exchange	25		(noun, verb)
eye	25		(noun, verb)
fire	25		(noun, verb)
position	25		(noun, verb)
pressure	25		(noun, verb)
stress	25		(noun, verb)
advantage	24		(noun, verb)
benefit	24		(noun, verb)
box	24		(noun, verb)
frame	24		(noun, verb)
issue	24		(noun, verb)
step	24		(noun, verb)
cycle	23		(noun, verb)
face	23		(noun, verb)
item	23		(noun, adverb)
metal	23		(noun, verb)
paint	23		(noun, verb)
review	23		(noun, verb)
room	23		(noun, verb)
screen	23		(noun, verb)
structure	23		(noun, verb)
view	23		(noun, verb)
account	22		(noun, verb)
ball	22		(noun, verb)
discipline	22		(noun, verb)
medium	22		(noun, adjective)
share	22		(noun, verb)
balance	21		(noun, verb)
bit	21		(noun, verb)
black	21		(noun, verb, adjective)
bottom	21		(noun, verb, adjective)
choice	21		(noun, adjective)
gift	21		(noun, verb)
impact	21		(noun, verb)
machine	21		(noun, verb)
shape	21		(noun, verb)
tool	21		(noun, verb)
wind	21		(noun, verb)
address	20		(noun, verb)
average	20		(noun, verb, adjective)
career	20		(noun, verb, adjective)
culture	20		(noun, verb)
morning	20		(noun, adverb)
pot	20		(noun, verb)
sign	20		(noun, verb)
table	20		(noun, verb)
task	20		(noun, verb)
condition	19		(noun, verb)
contact	19		(noun, verb)
credit	19		(noun, verb)
egg	19		(noun, verb)
hope	19		(noun, verb)
ice	19		(noun, verb)
network	19		(noun, verb)
north	19		(noun, adjective, adverb)
square	19		(noun, adjective, adverb)
attempt	18		(noun, verb)
date	18		(noun, verb)
effect	18		(noun, verb)
link	18		(noun, verb)
post	18		(noun, verb, adverb)
star	18		(noun, verb)
voice	18		(noun, verb)
capital	17		(noun, adjective)
challenge	17		(noun, verb, adjective)
friend	17		(noun, verb)
self	17		(noun, pronoun, adjective)
shot	17		(noun, adjective)
brush	16		(noun, verb)
couple	16		(noun, verb)
debate	16		(noun, verb)
exit	16		(noun, verb)
front	16		(noun, adjective, verb)
function	16		(noun, verb)
lack	16		(noun, verb)
living	16		(noun, adjective)
plant	16		(noun, verb)
plastic	16		(noun, adjective)
spot	16		(noun, verb)
summer	16		(noun, verb)
taste	16		(noun, verb)
theme	16		(noun, verb)
track	16		(noun, verb)
wing	16		(noun, verb)
brain	15		(noun, verb)
button	15		(noun, verb)
click	15		(noun, verb)
desire	15		(noun, verb)
foot	15		(noun, verb)
gas	15		(noun, verb)
influence	15		(noun, verb)
notice	15		(noun, verb)
rain	15		(noun, verb)
wall	15		(noun, verb)
base	14		(noun, verb, adjective)
damage	14		(noun, verb)
distance	14		(noun, verb)
feeling	14		(noun, adjective)
pair	14		(noun, verb)
savings	14		(noun, adjective, preposition)
staff	14		(noun, verb)
sugar	14		(noun, verb)
target	14		(noun, verb)
text	14		(noun, verb)
animal	13		(noun, adjective)
author	13		(noun, verb)
budget	13		(noun, adjective, verb)
discount	13		(noun, verb, adjective)
file	13		(noun, verb)
ground	13		(noun, verb, adjective)
lesson	13		(noun, verb)
minute	13		(noun, adjective, verb)
officer	13		(noun, verb)
phase	13		(noun, verb)
reference	13		(noun, verb, adjective)
register	13		(noun, verb)
sky	13		(noun, verb)
stage	13		(noun, verb)
stick	13		(noun, verb)
title	13		(noun, verb)
trouble	13		(noun, verb)
bowl	12		(noun, verb)
bridge	12		(noun, verb)
campaign	12		(noun, verb)
character	12		(noun, adjective, verb)
club	12		(noun, verb)
edge	12		(noun, verb, idiom)
evidence	12		(noun, verb, idiom)
fan	12		(noun, verb, idiom)
letter	12		(noun, verb, idiom)
lock	12		(noun, verb, idiom)
maximum	12		(noun, adjective)
novel	12		(noun, adjective)
option	12		(noun, verb)
pack	12		(noun, verb, adjective)
park	12		(noun, verb)
plenty	12		(noun, adjective, adverb)
quarter	12		(noun, verb, adjective)
skin	12		(noun, verb)
sort	12		(noun, verb)
weight	12		(noun, verb)
baby	11		(noun, verb, adjective)
background	11		(noun, adjective)
carry	11		(noun, verb)
dish	11		(noun, verb, idiom)
factor	11		(noun, verb)
fruit	11		(noun, verb)
glass	11		(noun, adjective, verb)
joint	11		(noun, adjective, verb)
master	11		(noun, adjective, verb)
muscle	11		(noun, verb, adjective)
red	11		(noun, adjective, idiom)
strength	11		(noun, idiom)
traffic	11		(noun, verb)
trip	11		(noun, verb, idiom)
vegetable	11		(noun, adjective)
appeal	10		(noun, verb)
chart	10		(noun, verb)
gear	10		(noun, verb, adjective)
ideal	10		(noun, adjective)
kitchen	10		(noun, adjective)
land	10		(noun, verb, idiom)
log	10		(noun, verb)
mother	10		(noun, adjective, verb)
net	10		(noun, verb)
party	10		(noun, adjective, verb)
principle	10		(noun, idiom)
relative	10		(noun, adjective)
sale	10		(noun, idiom)
season	10		(noun, verb, idiom)
signal	10		(noun, adjective, verb)
spirit	10		(noun, verb, idiom)
street	10		(noun, adjective, idiom)
tree	10		(noun, verb, idiom)
wave	10		(noun, verb, idiom)
belt	9		(noun, verb)
bench	9		(noun, verb)
commission	9		(noun, verb)
copy	9		(noun, verb, idiom)
drop	9		(noun, verb)
minimum	9		(noun, adjective)
path	9		(noun, idiom)
progress	9		(noun, verb, idiom)
project	9		(noun, verb)
sea	9		(noun, adjective, idiom)
south	9		(noun, adjective, adverb)
status	9		(noun, adjective)
stuff	9		(noun, verb)
ticket	9		(noun, verb, idiom)
tour	9		(noun, verb)
angle	8		(noun, verb)
blue	8		(noun, verb, adjective)
breakfast	8		(noun, verb)
confidence	8		(noun, idiom)
daughter	8		(noun, adjective)
degree	8		(noun, idiom)
doctor	8		(noun, verb)
dot	8		(noun, verb, idiom)
dream	8		(noun, verb, adjective)
duty	8		(noun, idiom)
essay	8		(noun, verb)
father	8		(noun, verb)
fee	8		(noun, verb)
finance	8		(noun, verb)
hour	8		(noun, adjective, idiom)
juice	8		(noun, verb, idiom)
limit	8		(noun, verb)
luck	8		(noun, verb, idiom)
milk	8		(noun, verb, idiom)
mouth	8		(noun, verb, idiom)
peace	8		(noun, interjection, verb)
pipe	8		(noun, verb)
seat	8		(noun, verb)
stable	8		(noun, verb)
storm	8		(noun, verb, idiom)
substance	8		(noun, idiom)
team	8		(noun, verb, adjective)
trick	8		(noun, adjective, verb)
afternoon	7		(noun, adjective)
bat	7		(noun, verb)
beach	7		(noun, verb)
blank	7		(noun, verb, adjective)
catch	7		(noun, verb)
chain	7		(noun, verb)
consideration	7		(noun, idiom)
cream	7		(noun, verb, adjective)
crew	7		(noun, verb)
detail	7		(noun, verb, idiom)
gold	7		(noun, adjective)
interview	7		(noun, verb)
kid	7		(noun, verb, adjective)
mark	7		(noun, verb, idiom)
match	7		(noun, verb)
mission	7		(noun, adjective)
pain	7		(noun, verb, idiom)
pleasure	7		(noun, verb)
score	7		(noun, verb, idiom)
screw	7		(noun, verb, idiom)
sex	7		(noun, verb, idiom)
shop	7		(noun, verb, interjection)
shower	7		(noun, verb, idiom)
suit	7		(noun, verb, idiom)
tone	7		(noun, verb)
window	7		(noun, verb)
agent	6		(noun, adjective, verb)
band	6		(noun, verb)
block	6		(noun, verb)
bone	6		(noun, verb, adverb)
calendar	6		(noun, verb)
cap	6		(noun, verb)
coat	6		(noun, verb)
contest	6		(noun, verb)
corner	6		(noun, adjective, verb)
court	6		(noun, verb, idiom)
cup	6		(noun, verb)
district	6		(noun, verb)
door	6		(noun, idiom)
east	6		(noun, adjective, adverb)
finger	6		(noun, verb, idiom)
garage	6		(noun, verb)
guarantee	6		(noun, verb)
hole	6		(noun, verb, idiom)
hook	6		(noun, verb, idiom)
implement	6		(noun, verb)
layer	6		(noun, verb)
lecture	6		(noun, verb)
lie	6		(noun, verb, idiom)
manner	6		(noun, idiom)
meeting	6		(noun, idiom)
nose	6		(noun, verb, idiom)
parking	6		(noun, adjective)
partner	6		(noun, verb)
profile	6		(noun, verb)
respect	6		(noun, verb)
rice	6		(noun, verb)
routine	6		(noun, adjective)
schedule	6		(noun, verb)
swimming	6		(noun, adjective)
telephone	6		(noun, verb)
tip	6		(noun, verb)
winter	6		(noun, adjective, verb)
airline	5		(noun, adjective)
bag	5		(noun, verb)
battle	5		(noun, verb)
bed	5		(noun, verb)
bill	5		(noun, verb)
bother	5		(noun, verb)
cake	5		(noun, verb)
code	5		(noun, verb)
curve	5		(noun, verb, idiom)
designer	5		(noun, adjective)
dimension	5		(noun, verb)
dress	5		(noun, adjective, verb)
ease	5		(noun, verb)
emergency	5		(noun, adjective)
evening	5		(noun, adjective)
extension	5		(noun, adjective)
farm	5		(noun, verb, idiom)
fight	5		(noun, verb)
gap	5		(noun, verb)
grade	5		(noun, verb)
holiday	5		(noun, adjective, verb)
horror	5		(noun, adjective)
horse	5		(noun, verb, adjective)
host	5		(noun, verb)
husband	5		(noun, verb)
loan	5		(noun, verb, idiom)
mistake	5		(noun, verb, idiom)
mountain	5		(noun, adjective, idiom)
nail	5		(noun, verb, idiom)
noise	5		(noun, verb)
occasion	5		(noun, verb, idiom)
package	5		(noun, verb)
patient	5		(noun, adjective)
pause	5		(noun, verb, idiom)
phrase	5		(noun, verb)
proof	5		(noun, adjective, verb)
race	5		(noun, verb)
relief	5		(noun, idiom)
sand	5		(noun, verb, idiom)
sentence	5		(noun, verb)
shoulder	5		(noun, verb, idiom)
smoke	5		(noun, verb, idiom)
stomach	5		(noun, verb)
string	5		(noun, verb, idiom)
tourist	5		(noun, adverb)
towel	5		(noun, verb)
vacation	5		(noun, verb)
west	5		(noun, adjective, adverb)
wheel	5		(noun, verb, idiom)
wine	5		(noun, adjective, verb)
arm	4		(noun, verb)
aside	4		(noun, adverb)
associate	4		(noun, verb, adjective)
bet	4		(noun, verb)
blow	4		(noun, verb)
border	4		(noun, verb)
branch	4		(noun, verb)
breast	4		(noun, verb)
brother	4		(noun, interjection)
buddy	4		(noun, verb)
bunch	4		(noun, verb)
chip	4		(noun, verb)
coach	4		(noun, verb, adverb)
cross	4		(noun, verb, adjective)
document	4		(noun, verb)
draft	4		(noun, verb, adjective)
dust	4		(noun, verb)
expert	4		(noun, adjective)
floor	4		(noun, verb)
god	4		(noun, interjection)
golf	4		(noun, verb)
habit	4		(noun, verb)
iron	4		(noun, verb)
judge	4		(noun, verb)
knife	4		(noun, verb)
landscape	4		(noun, verb)
league	4		(noun, verb)
mail	4		(noun, verb)
mess	4		(noun, verb)
native	4		(noun, adjective)
opening	4		(noun, adjective)
parent	4		(noun, verb)
pattern	4		(noun, verb)
pin	4		(noun, verb)
pool	4		(noun, verb)
pound	4		(noun, verb)
request	4		(noun, verb)
salary	4		(noun, verb)
shame	4		(noun, verb)
shelter	4		(noun, verb)
shoe	4		(noun, verb)
silver	4		(noun, adjective, verb)
tackle	4		(noun, verb)
tank	4		(noun, verb)
trust	4		(noun, verb)
assist	3		(noun, verb)
bake	3		(noun, verb)
bar	3		(noun, verb, preposition)
bell	3		(noun, verb)
bike	3		(noun, verb)
blame	3		(noun, verb)
boy	3		(noun, interjection)
brick	3		(noun, verb)
chair	3		(noun, verb)
closet	3		(noun, verb, adjective)
clue	3		(noun, verb)
collar	3		(noun, verb)
comment	3		(noun, verb)
conference	3		(noun, verb)
devil	3		(noun, verb)
diet	3		(noun, verb)
fear	3		(noun, verb)
fuel	3		(noun, verb)
glove	3		(noun, verb)
jacket	3		(noun, verb)
lunch	3		(noun, verb)
monitor	3		(noun, verb)
mortgage	3		(noun, verb)
nurse	3		(noun, verb)
pace	3		(noun, verb, preposition)
panic	3		(noun, verb)
peak	3		(noun, verb, adjective)
plane	3		(noun, adjective, verb)
reward	3		(noun, verb)
row	3		(noun, verb)
sandwich	3		(noun, verb)
shock	3		(noun, verb)
spite	3		(noun, verb)
spray	3		(noun, verb)
surprise	3		(noun, verb)
till	3		(noun, verb)
transition	3		(noun, verb)
weekend	3		(noun, verb)
welcome	3		(noun, interjection, verb)
yard	3		(noun, verb)
alarm	2		(noun, verb)
bend	2		(noun, verb)
bicycle	2		(noun, verb)
bite	2		(noun, verb)
blind	2		(noun, verb, adjective)
bottle	2		(noun, verb)
cable	2		(noun, verb)
candle	2		(noun, verb)
clerk	2		(noun, verb)
cloud	2		(noun, verb)
concert	2		(noun, verb)
counter	2		(noun, verb, adverb)
flower	2		(noun, verb)
grandfather	2		(noun, verb)
harm	2		(noun, verb)
knee	2		(noun, verb)
lawyer	2		(noun, verb)
leather	2		(noun, adjective, verb)
load	2		(noun, verb)
mirror	2		(noun, verb)
neck	2		(noun, verb)
pension	2		(noun, verb)
plate	2		(noun, verb)
purple	2		(noun, adjective, verb)
ruin	2		(noun, verb)
ship	2		(noun, verb)
skirt	2		(noun, verb)
slice	2		(noun, verb)
snow	2		(noun, verb)
specialist	2		(noun, adjective)
stroke	2		(noun, verb)
switch	2		(noun, verb)
trash	2		(noun, verb)
tune	2		(noun, verb)
zone	2		(noun, verb)
anger	1		(noun, verb)
award	1		(noun, verb)
bid	1		(noun, verb)
bitter	1		(noun, adjective)
boot	1		(noun, verb)
bug	1		(noun, verb)
camp	1		(noun, verb, adjective)
candy	1		(noun, verb)
carpet	1		(noun, verb)
cat	1		(noun, verb)
champion	1		(noun, verb)
channel	1		(noun, verb)
clock	1		(noun, verb)
comfort	1		(noun, verb)
cow	1		(noun, verb)
crack	1		(noun, verb, adjective)
engineer	1		(noun, verb)
entrance	1		(noun, verb)
fault	1		(noun, verb)
grass	1		(noun, verb)
guy	1		(noun, verb)
hell	1		(noun, interjection)
highlight	1		(noun, verb)
incident	1		(noun, adjective)
island	1		(noun, verb)
joke	1		(noun, verb)
jury	1		(noun, verb, adjective)
leg	1		(noun, verb)
lip	1		(noun, verb)
mate	1		(noun, verb)
motor	1		(noun, adjective, verb)
nerve	1		(noun, verb)
passage	1		(noun, verb)
pen	1		(noun, verb)
pride	1		(noun, verb)
priest	1		(noun, verb)
prize	1		(noun, adjective, verb)
promise	1		(noun, verb)
resident	1		(noun, adjective)
resort	1		(noun, verb)
ring	1		(noun, verb)
roof	1		(noun, verb)
rope	1		(noun, verb)
sail	1		(noun, verb)
scheme	1		(noun, verb)
script	1		(noun, verb)
sock	1		(noun, verb)
station	1		(noun, verb)
toe	1		(noun, verb)
tower	1		(noun, verb)
truck	1		(noun, verb)
witness	1		(noun, verb)
a	4506		(indefinite article, noun, preposition)
you	2041		(pronoun, noun)
it	1386		(pronoun, noun)
can	895		(auxiliary verb, noun)
will	577		(auxiliary verb, noun)
if	546		(conjunction, noun)
one	441		(adjective, noun, pronoun)
many	397		(adjective, noun, pronoun)
most	378		(adjective, noun, adverb)
other	369		(adjective, noun, pronoun)
use	319		(verb, noun)
make	262		(verb, noun)
good	201		(adjective, noun, adverb)
look	144		(verb, noun, interjection)
help	141		(verb, noun, interjection)
go	131		(verb, noun, adjective)
great	126		(adjective, noun, adverb)
being	124		(verb, noun)
few	117		(adjective, noun, pronoun)
might	116		(auxiliary verb, noun)
still	112		(adjective, noun, adverb)
public	97		(adjective, noun)
read	97		(verb, noun)
keep	96		(verb, noun)
start	96		(verb, noun)
give	93		(verb, noun)
human	92		(adjective, noun)
local	90		(adjective, noun)
general	85		(adjective, noun)
she	85		(pronoun, noun)
specific	83		(adjective, noun)
long	82		(adjective, noun, adverb)
play	75		(verb, noun)
feel	74		(verb, noun)
high	74		(adjective, noun, adverb)
tonight	71		(adverb, noun)
put	70		(verb, noun)
common	69		(adjective, noun)
set	69		(verb, noun, adjective)
change	67		(verb, noun)
simple	63		(adjective, noun)
past	60		(adjective, noun, preposition)
big	59		(adjective, noun)
possible	59		(adjective, noun)
particular	58		(adjective, noun)
today	54		(adverb, noun)
major	53		(adjective, noun, verb)
personal	53		(adjective, noun)
current	52		(adjective, noun)
national	52		(adjective, noun)
cut	50		(verb, noun)
natural	50		(adjective, noun, adverb)
physical	50		(adjective, noun)
show	50		(verb, noun)
try	50		(verb, noun)
check	49		(verb, noun, interjection)
second	49		(number, noun)
call	47		(verb, noun)
move	47		(verb, noun)
pay	47		(verb, noun)
let	46		(verb, noun)
increase	45		(verb, noun)
single	45		(adjective, noun, verb)
individual	44		(adjective, noun)
turn	44		(verb, noun)
ask	42		(verb, noun)
buy	42		(verb, noun)
guard	42		(verb, noun)
hold	42		(verb, noun)
main	42		(adjective, noun)
offer	42		(verb, noun)
potential	42		(adjective, noun)
professional	42		(adjective, noun)
international	41		(adjective, noun)
travel	41		(verb, noun)
cook	40		(verb, noun)
alternative	39		(adjective, noun)
following	39		(preposition, noun, adjective)
special	39		(adjective, noun)
working	39		(adjective, noun)
whole	38		(adjective, noun, adverb)
dance	37		(verb, noun)
excuse	37		(verb, noun)
cold	34		(adjective, noun, adverb)
commercial	34		(adjective, noun)
low	34		(adjective, noun, adverb)
purchase	34		(verb, noun)
deal	33		(verb, noun)
primary	33		(adjective, noun)
worth	33		(adjective, noun)
fall	32		(verb, noun)
necessary	31		(adjective, noun)
positive	31		(adjective, noun)
produce	31		(verb, noun)
search	31		(verb, noun)
present	30		(adjective, noun, verb)
spend	30		(verb, noun)
talk	30		(verb, noun)
creative	29		(adjective, noun)
tell	29		(verb, noun)
cost	28		(verb, noun)
drive	28		(verb, noun)
green	28		(adjective, noun, verb)
support	28		(verb, noun)
glad	27		(adjective, noun)
remove	27		(verb, noun)
return	27		(verb, noun)
run	27		(verb, noun)
complex	26		(adjective, noun, verb)
due	26		(adjective, noun, adverb)
effective	26		(adjective, noun)
middle	26		(adjective, noun)
regular	26		(adjective, noun)
reserve	26		(verb, noun)
independent	25		(adjective, noun)
leave	25		(verb, noun)
original	25		(adjective, noun)
reach	25		(verb, noun)
rest	25		(verb, noun)
serve	25		(verb, noun)
watch	25		(verb, noun)
beautiful	24		(adjective, noun, interjection)
charge	24		(verb, noun)
active	23		(adjective, noun)
break	23		(verb, noun)
negative	23		(adjective, noun, interjection)
safe	23		(adjective, noun)
stay	23		(verb, noun)
visit	23		(verb, noun)
visual	23		(adjective, noun)
affect	22		(verb, noun)
cover	22		(verb, noun)
report	22		(verb, noun)
rise	22		(verb, noun)
walk	21		(verb, noun)
white	21		(adjective, noun, verb)
beyond	20		(preposition, noun)
junior	20		(adjective, noun)
pick	20		(verb, noun)
unique	20		(adjective, noun)
anything	19		(pronoun, noun, adverb)
classic	19		(adjective, noun)
final	19		(adjective, noun)
lift	19		(verb, noun)
mix	19		(verb, noun)
private	19		(adjective, noun)
stop	19		(verb, noun)
teach	19		(verb, noun)
western	19		(adjective, noun)
concern	18		(verb, noun)
familiar	18		(adjective, noun)
fly	18		(verb, noun)
official	18		(adjective, noun)
broad	17		(adjective, noun)
comfortable	17		(adjective, noun)
gain	17		(verb, noun)
maybe	17		(adverb, noun)
rich	17		(adjective, noun)
save	17		(verb, noun, preposition)
stand	17		(verb, noun)
young	17		(adjective, noun)
fail	16		(verb, noun)
heavy	16		(adjective, noun, adverb)
hello	16		(interjection, noun)
lead	16		(verb, noun)
listen	16		(verb, noun)
valuable	16		(adjective, noun)
worry	16		(verb, noun)
handle	15		(verb, noun)
leading	15		(adjective, noun)
meet	15		(verb, noun)
release	15		(verb, noun)
sell	15		(verb, noun)
finish	14		(verb, noun)
normal	14		(adjective, noun)
press	14		(verb, noun)
ride	14		(verb, noun)
secret	14		(adjective, noun)
spread	14		(verb, noun)
spring	14		(verb, noun)
tough	14		(adjective, noun)
wait	14		(verb, noun)
brown	13		(adjective, noun, verb)
deep	13		(adjective, noun, adverb)
display	13		(verb, noun)
flow	13		(verb, noun)
hit	13		(verb, noun)
objective	13		(adjective, noun)
shoot	13		(verb, noun, interjection)
touch	13		(verb, noun)
cancel	12		(verb, noun)
chemical	12		(adjective, noun)
cry	12		(verb, noun, idiom)
dump	12		(verb, noun, idiom)
extreme	12		(adjective, noun)
push	12		(verb, noun, idiom)
conflict	11		(verb, noun)
eat	11		(verb, noun, idiom)
fill	11		(verb, noun, idiom)
formal	11		(adjective, noun, adverb)
jump	11		(verb, noun, adjective)
kick	11		(verb, noun, idiom)
opposite	11		(adjective, noun, preposition)
pass	11		(verb, noun, idiom)
pitch	11		(verb, noun)
remote	11		(adjective, noun)
total	11		(adjective, noun, verb)
treat	11		(verb, noun)
vast	11		(adjective, noun)
abuse	10		(verb, noun)
beat	10		(verb, noun, adjective)
burn	10		(verb, noun)
deposit	10		(verb, noun)
print	10		(verb, noun, adjective)
raise	10		(verb, noun, idiom)
sleep	10		(verb, noun, idiom)
somewhere	10		(adverb, noun)
advance	9		(verb, noun, adjective)
anywhere	9		(adverb, noun)
consist	9		(verb, noun)
dark	9		(adjective, noun, idiom)
double	9		(adjective, noun, verb)
draw	9		(verb, noun, idiom)
equal	9		(adjective, noun, verb)
fix	9		(verb, noun, idiom)
hire	9		(verb, noun, adjective)
internal	9		(adjective, noun)
join	9		(verb, noun)
kill	9		(verb, noun, idiom)
sensitive	9		(adjective, noun)
tap	9		(verb, noun)
win	9		(verb, noun)
attack	8		(verb, noun)
claim	8		(verb, noun)
constant	8		(adjective, noun)
drag	8		(verb, noun, adjective)
drink	8		(verb, noun)
guess	8		(verb, noun, idiom)
minor	8		(adjective, noun, verb)
pull	8		(verb, noun)
raw	8		(adjective, noun, idiom)
soft	8		(adjective, noun, adverb)
solid	8		(adjective, noun)
wear	8		(verb, noun, idiom)
weird	8		(adjective, noun)
wonder	8		(verb, noun, idiom)
annual	7		(adjective, noun)
count	7		(verb, noun, adjective)
dead	7		(adjective, noun, adverb)
doubt	7		(verb, noun, idiom)
feed	7		(verb, noun, idiom)
forever	7		(adverb, noun, idiom)
impress	7		(verb, noun)
nobody	7		(pronoun, noun)
repeat	7		(verb, noun)
round	7		(adjective, noun, adverb)
sing	7		(verb, noun)
slide	7		(verb, noun, idiom)
strip	7		(verb, noun)
whereas	7		(conjunction, noun)
wish	7		(verb, noun)
combine	6		(verb, noun)
command	6		(verb, noun)
dig	6		(verb, noun)
divide	6		(verb, noun)
equivalent	6		(adjective, noun)
hang	6		(verb, noun, idiom)
hunt	6		(verb, noun)
initial	6		(adjective, noun, verb)
march	6		(verb, noun, idiom)
mention	6		(verb, noun, idiom)
smell	6		(verb, noun)
spiritual	6		(adjective, noun)
survey	6		(verb, noun)
tie	6		(verb, noun, idiom)
adult	5		(adjective, noun)
brief	5		(adjective, noun, verb)
crazy	5		(adjective, noun, idiom)
escape	5		(verb, noun, adjective)
gather	5		(verb, noun, idiom)
hate	5		(verb, noun)
prior	5		(adjective, noun, idiom)
repair	5		(verb, noun)
rough	5		(adjective, noun, adverb)
sad	5		(adjective, noun)
scratch	5		(verb, noun, adjective)
sick	5		(adjective, noun, idiom)
strike	5		(verb, noun, adjective)
employ	4		(verb, noun)
external	4		(adjective, noun)
hurt	4		(verb, noun)
illegal	4		(adjective, noun)
laugh	4		(verb, noun)
lay	4		(verb, noun, adjective)
mobile	4		(adjective, noun)
nasty	4		(adjective, noun)
ordinary	4		(adjective, noun)
respond	4		(verb, noun)
royal	4		(adjective, noun)
senior	4		(adjective, noun)
split	4		(verb, noun)
strain	4		(verb, noun)
struggle	4		(verb, noun)
swim	4		(verb, noun)
train	4		(verb, noun)
upper	4		(adjective, noun)
wash	4		(verb, noun)
yellow	4		(adjective, noun, verb)
convert	3		(verb, noun)
crash	3		(verb, noun, adjective)
dependent	3		(adjective, noun)
fold	3		(verb, noun)
funny	3		(adjective, noun)
grab	3		(verb, noun)
hide	3		(verb, noun)
miss	3		(verb, noun)
permit	3		(verb, noun)
quote	3		(verb, noun)
recover	3		(verb, noun)
resolve	3		(verb, noun)
roll	3		(verb, noun)
sink	3		(verb, noun)
slip	3		(verb, noun)
spare	3		(adjective, noun, verb)
suspect	3		(verb, noun, adjective)
sweet	3		(adjective, noun)
swing	3		(verb, noun)
twist	3		(verb, noun)
upstairs	3		(adjective, noun)
usual	3		(adjective, noun)
abroad	2		(adverb, noun)
brave	2		(adjective, noun, verb)
calm	2		(adjective, noun, verb)
concentrate	2		(verb, noun)
estimate	2		(verb, noun)
grand	2		(adjective, noun)
male	2		(adjective, noun)
mine	2		(pronoun, noun, verb)
prompt	2		(verb, noun, adjective)
quiet	2		(adjective, noun, verb)
refuse	2		(verb, noun)
regret	2		(verb, noun)
reveal	2		(verb, noun)
rush	2		(verb, noun)
shake	2		(verb, noun)
shift	2		(verb, noun)
shine	2		(verb, noun)
steal	2		(verb, noun)
suck	2		(verb, noun)
surround	2		(verb, noun)
anybody	1		(pronoun, noun)
bear	1		(verb, noun)
brilliant	1		(adjective, noun)
dare	1		(verb, noun)
dear	1		(adjective, noun, adverb)
delay	1		(verb, noun)
drunk	1		(adjective, noun)
female	1		(adjective, noun)
hurry	1		(verb, noun)
inevitable	1		(adjective, noun)
invite	1		(verb, noun)
kiss	1		(verb, noun)
neat	1		(adjective, noun)
pop	1		(verb, noun, adverb)
punch	1		(verb, noun)
quit	1		(verb, noun)
reply	1		(verb, noun)
representative	1		(adjective, noun)
resist	1		(verb, noun)
rip	1		(verb, noun)
rub	1		(verb, noun)
silly	1		(adjective, noun)
smile	1		(verb, noun)
spell	1		(verb, noun)
stretch	1		(verb, noun)
stupid	1		(adjective, noun)
tear	1		(verb, noun)
temporary	1		(adjective, noun)
tomorrow	1		(adverb, noun)
wake	1		(verb, noun)
wrap	1		(verb, noun)
yesterday	1		(adverb, noun)

ENDOFLIST'''

words = string.split()
i = 0

while words[i] != 'ENDOFLIST':

  #checks to see if the fist char of the string is a letter
  #need to be careful with the Exceptions like verb) and so on maybe 
  #should search for verb letters or something in the word and if it  
  #contins it rmove the word. Or could check through list for every 
  #case FIXED the rough way NEED to do for adverb tho
  if (65 <= ord(words[i][0]) <= 90 or 97 <= ord(words[i][0]) <= 122) 
  and (words[i] != 'idiom)' 
  and words[i] != '(idiom,' 
  and words[i] != 'verb)' 
  and words[i] != '(verb,'
  and words[i] != 'noun)' 
  and words[i] != '(noun,' 
  and words[i] != 'noun,' 
  and words[i] != 'verb,'
  and words[i] != 'idiom,'):
    i += 1
    
  else:
    del words[i]
    i -= 1
    

print(words)
