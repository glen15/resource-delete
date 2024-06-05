import boto3

### 지워야하는 리소스 키워드 ###
keyword = "TARGET KEYWORD"

### 대상 리전 지정 ###
region_name = 'TARGET REGION'

def delete_dynamodb_tables(keyword):
    # 서울 리전 세션 생성
    session = boto3.Session(region_name=region_name)
    
    # DynamoDB 클라이언트 생성
    dynamodb = session.client('dynamodb')
    
    # DynamoDB 테이블 목록 가져오기
    response = dynamodb.list_tables()
    
    print("시작\n\n\n")
    # 이름에 키워드가 포함된 테이블 찾기
    tables_to_delete = [table_name for table_name in response.get('TableNames', []) if keyword in table_name.lower()]
    
    if tables_to_delete:
        print("찾은 DynamoDB 테이블 목록:")
        for table_name in tables_to_delete:
            print(f"- {table_name}")
        
        confirmation = input("이 모든 DynamoDB 테이블을 삭제하시겠습니까? (y/n): ").strip().lower()
        if confirmation == 'y':
            for table_name in tables_to_delete:
                print(f"\n\nDynamoDB 테이블 삭제 중: {table_name}")
                dynamodb.delete_table(TableName=table_name)
        else:
            for table_name in tables_to_delete:
                confirmation = input(f"DynamoDB 테이블 '{table_name}'을(를) 삭제하시겠습니까? (y/n): ").strip().lower()
                if confirmation == 'y':
                    print(f"\n\nDynamoDB 테이블 삭제 중: {table_name}")
                    dynamodb.delete_table(TableName=table_name)
    else:
        print("지정된 키워드가 포함된 테이블을 찾을 수 없습니다.")
    
    print("\n\n\n종료")

if __name__ == '__main__':
    delete_dynamodb_tables(keyword)
