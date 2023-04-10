# [Golang]优雅实现「业务/权限」检查

## 业务场景
对一些业务进行检查，比如权限检查，审核检查等。
## 实现思路
1. 对应权限用“枚举”定义，由于Golang没有枚举，所以用常量和后面的map代替。常量定义如下
```golang
const (
	PermitZero 	= 0
	PermitOne   = 1
	PermitTwo   = 2
	PermitThree = 3
	...
)
```
2. 定义Check方法，每个Check方法参数一致，返回一致。
```golang
type CheckParams struct {
	p1	string
	p2	int64
	p3	Context
	...
}

func CheckZero(p *CheckParams) error {}
func CheckOne(p *CheckParams) error {}
func CheckTwo(p *CheckParams) error {}
func CheckThree(p *CheckParams) error {}
...
```
3. 把权限顺序放入列表里，对权限与函数进行map对应
```golang
var (
	CheckFunc = map[int]func(*CheckParams) error {
		PermitZero: 	CheckZero,
		PermitOne: 		CheckOne,
		PermitTwo: 		CheckTwo,
		PermitThree: 	CheckThree,
		...
	}

	CheckOrder = []int {
		PermitZero 	= 0
		PermitOne   = 1
		PermitTwo   = 2
		PermitThree = 3	
		...
	}
)
```
4. 业务逻辑编写，遍历CheckOrder，通过位检查权限中是否需要检查当前项目，调用Check函数检查
```golang
func IsSet(s uint64, b int) uint64 {
	return s & (1 << b)
}

for _, index := range CheckOrder {
	if IsSet(permit, index) != 0 {
		baseRet := CheckFunc[index](params)
		if baseRet != nil {
			log.Error(...)
			return 
		}
	}
}
```


