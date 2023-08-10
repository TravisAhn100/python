

def icbm_research(name, power):
    print(f"대륙칸탄도발사체 {name}(을)를 렬심히 련구 중에 있읍니다. 위력은 {power}입네다.")

def icbm_manufacture(name, power):
    print(f"대륙칸탄도발사체 {name}(을)를 제작했읍니다. 위력은 {power}입네다.")

def icbm_project(leader, name, power):
    icbm_research(name, power)
    icbm_manufacture(name, power)
    print(f"우리의 위대한 령도자 {leader}의 힘으로 {name}을 남조선 갓나새끼들에게 발사합네다.")

icbm_project("김정은", "대포동 19호", "일천만 티 엔 티")