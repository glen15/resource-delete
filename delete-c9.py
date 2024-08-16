import boto3

# 지워야하는 리소스 키워드
keyword = ""

# 대상 리전 지정
region = "ap-northeast-2"  # 서울 리전

def delete_cloud9_environments(keyword, region):
    # 지정된 리전으로 세션 생성
    session = boto3.Session(region_name=region)
    
    # Cloud9 클라이언트 생성
    cloud9 = session.client('cloud9')
    
    print(f"시작 (리전: {region})\n\n\n")
    
    # Cloud9 환경 목록 가져오기
    environments_to_delete = []
    next_token = None
    
    while True:
        if next_token:
            response = cloud9.list_environments(nextToken=next_token, maxResults=25)
        else:
            response = cloud9.list_environments(maxResults=25)
        
        environment_ids = response['environmentIds']
        
        # 키워드로 시작하는 환경 찾기
        for env_id in environment_ids:
            env_info = cloud9.describe_environments(environmentIds=[env_id])['environments'][0]
            if env_info['name'].lower().startswith(keyword.lower()):
                environments_to_delete.append((env_id, env_info['name']))
        
        if 'nextToken' in response:
            next_token = response['nextToken']
        else:
            break
    
    if environments_to_delete:
        print(f"찾은 Cloud9 환경 목록 (리전: {region}):")
        for env_id, env_name in environments_to_delete:
            print(f"- {env_name} (ID: {env_id})")
        
        confirmation = input("이 모든 Cloud9 환경을 삭제하시겠습니까? (y/n): ").strip().lower()
        if confirmation == 'y':
            for env_id, env_name in environments_to_delete:
                print(f"\n\nCloud9 환경 삭제 중: {env_name} (ID: {env_id})")
                try:
                    cloud9.delete_environment(environmentId=env_id)
                    print(f"Cloud9 환경이 삭제되었습니다: {env_name}")
                except Exception as e:
                    print(f"오류 발생: {env_name} 삭제 실패 - {str(e)}")
        else:
            for env_id, env_name in environments_to_delete:
                confirmation = input(f"\n\nCloud9 환경 '{env_name}'을(를) 삭제하시겠습니까? (y/n): ").strip().lower()
                if confirmation == 'y':
                    print(f"\n\nCloud9 환경 삭제 중: {env_name} (ID: {env_id})")
                    try:
                        cloud9.delete_environment(environmentId=env_id)
                        print(f"Cloud9 환경이 삭제되었습니다: {env_name}")
                    except Exception as e:
                        print(f"오류 발생: {env_name} 삭제 실패 - {str(e)}")
    else:
        print(f"지정된 키워드로 시작하는 Cloud9 환경을 찾을 수 없습니다. (리전: {region})")
    
    print("\n\n\n종료")

if __name__ == '__main__':
    delete_cloud9_environments(keyword, region)
