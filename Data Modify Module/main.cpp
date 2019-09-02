/*
    **********************************
    *                                *
    *  Modify Raw_Data by codeup38   *
    *                                *
    **********************************
*/

#include <cstdio>
#include <cstring>
#include <algorithm>

typedef struct __str{

    char ID[30];
    char checkSolve[7000];
    int countSuccess;
    int countFailSubmit;
    int totalSubmit;

    bool isOccupied;
    /*
        * ID = 회원 ID 저장
        * checkSolve = 해당 문제 번호를 인덱스로 사용.
        (해당 기간 동안) 0은 풀지 않음을, 1은 풀었음을 의미함.
        * countSuccess = 정확한 풀이가 몇 번 나왔는지를 의미함.(해당 기간 내 중복 제외)
        * countFailSubmit = 정확한 풀이 이외의 결과가 나온 횟수를 의미함.
        * totalSubmit = 몇번 제출했는지 확인하는데 사용.
        * isOccupied = 이미 정보가 입력된 인덱스인지 확인하는 데에 사용.
    */
}ident;

typedef struct __problem{

    int num;
    int submit;
    /*
        * num = 문제 번호
        * submit = 해당 문제 제출 횟수
    */
}prob;


ident check[30001]; // check[] 선언
prob probSub[7000];

int idlimit;

void clearStruct() // 초기화 해주는 함수
{
    for(int i=0; i<30001; i++) {
        for(int k=0; k<7000; k++) {

            if(k<30) check[i].ID[k] = check[i].checkSolve[k] = 0;
            else check[i].checkSolve[k] = 0;
        }

        check[i].isOccupied = false;
        check[i].totalSubmit =
        check[i].countFailSubmit =
        check[i].countSuccess = 0;

    }

    for(int i=0; i<7000; i++) probSub[i].num = i, probSub[i].submit = 0;

    return;
}

bool compareAC(ident a, ident b)
{
    if(a.countSuccess == b.countSuccess) return a.countFailSubmit <= b.countFailSubmit;
    else return a.countSuccess > b.countSuccess;
}

bool compareSub(ident a, ident b)
{
    if(a.totalSubmit == b.totalSubmit) return a.countSuccess >= b.countSuccess;
    else return a.totalSubmit > b.totalSubmit;
}

bool compareFail(ident a, ident b)
{
    if(a.countFailSubmit == b.countFailSubmit) return a.totalSubmit >= b.totalSubmit;
    else return a.countFailSubmit > b.countFailSubmit;
}

bool compareProb(prob a, prob b) {  if(a.submit == b.submit) return a.num > b.num;
                                          else return a.submit > b.submit; }

void printAcList() // AC 순위 순서대로 출력
{
    FILE *printAC = fopen("Rank List/AC_Rank.txt","w");

    std::sort(check, check + idlimit, compareAC);

    for(int i = 0; i < idlimit; i++) {
        if(check[i].countSuccess == 0) break;

        fprintf(printAC,"|%d|%s|%d|\n", i+1, check[i].ID, check[i].countSuccess);
    }

    fclose(printAC);

    return;
}

void printSubmitList() // 제출 횟수 순서대로 출력 (중복 포함)
{
    FILE *printSub = fopen("Rank List/Total_Submit_Rank.txt","w");

    std::sort(check, check + idlimit, compareSub);

    for(int i = 0; i < idlimit; i++) {
        if(check[i].totalSubmit == 0) break;

        fprintf(printSub,"|%d|%s|%d|\n", i+1, check[i].ID, check[i].totalSubmit);
    }

    fclose(printSub);

    return;
}

void printFailList() // 트롤 순서대로 출력(틀린 개수 순서)
{
    FILE *printFail = fopen("Rank List/Troll_Rank.txt","w");

    std::sort(check, check + idlimit, compareFail);

    for(int i = 0; i < idlimit; i++) {
        if(check[i].countFailSubmit == 0) break;

        fprintf(printFail,"|%d|%s|%d|\n", i+1, check[i].ID, check[i].countFailSubmit);
    }

    fclose(printFail);

    return;
}

void printProblemList() // 제출 많이 한 문제 순서대로 출력
{
    FILE *printProblem = fopen("Rank List/Problem_Rank.txt","w");

    std::sort(probSub, probSub + 7000, compareProb);

    for(int i = 0; i < 7000; i++) {
        if(probSub[i].submit == 0) break;

        fprintf(printProblem,"|%d|%d|%d|\n", i+1, probSub[i].num, probSub[i].submit);
    }

    fclose(printProblem);

    return;
}

void printProblemSkipList() // 제출 많이 한 문제 순서대로 출력, ** 단 1000번대 문제는 제외 **
{
    FILE *printSkipProblem = fopen("Rank List/Problem_Skip_Rank.txt","w");

    std::sort(probSub, probSub + 7000, compareProb);

    int ranked = 1;

    for(int i = 0; i < 7000; i++) {
        if(probSub[i].submit == 0) break;

        if(probSub[i].num >= 2000) fprintf(printSkipProblem, "|%d|%d|%d|\n", ranked++, probSub[i].num, probSub[i].submit);
    }

    fclose(printSkipProblem);

    return;
}

int main()
{
    FILE *readF = fopen("raw_data.txt","r");

    int submitNum, problemNum, memory, time, byte, submitCount = 0, index = 0;
    char inputID[30], submitRes[20], lang[10], submitTime[20];
    bool noMatch = true;

    clearStruct();

    /*
        About Variables ::

        <int>
        * submitNum = 제출 번호
        * problemNum = 문제 번호
        * memory = 사용한 메모리
        * time = 소스 코드 실행 시간
        * byte = 소스 코드 길이(B)
        * submitCount = 크롤링한 제출 기록 개수

        <char>
        * inputID[30] = 회원 ID
        * submitRes[10] = 채점 결과
        * lang[7] = 사용 언어
        * submitTime[8] = 제출 시간 { ** 변수 time과 혼동하지 말 것 ** }
    */

    int inputDataCheck;

    puts("Input data에 문제가 없음을 확인하였습니까?\n확인하였으면 1, 확인하지 않았으면 0을 눌러주세요.");
    printf(": "); scanf("%d", &inputDataCheck);

    if(inputDataCheck == 0) { puts("확인 부탁드리며, 프로그램은 종료됩니다."); fflush(stdin); getchar(); return 0; }


    while(~fscanf(readF,"%d %s  %d %s %d %d %s %d B %[^\n]s ", &submitNum, inputID, &problemNum, submitRes, &memory, &time, lang, &byte, submitTime)) {

        /*
            raw_data.txt 데이터 누락 확인 필수
            종종 제출 시간이 누락되는 경우 있음
        */

        probSub[problemNum].submit++;

        while(check[index].isOccupied == true) {

            if(!strcmp(check[index].ID,inputID)) {
                if(check[index].checkSolve[problemNum]) { check[index].totalSubmit++; index++; noMatch = false; break; }

                if(!strcmp(submitRes,"정확한풀이")) check[index].checkSolve[problemNum] = 1, check[index].countSuccess++;
                else check[index].countFailSubmit++;


                check[index].totalSubmit++;

                index++;
                noMatch = false;
                break;
            }

            index >= 30000 ? puts("범위를 넘어섰습니다. Ctrl-C로 정지시킨 후 check[]의 크기를 늘려주세요.") : index++;
        }

        if(!index || (noMatch == true)) {
            check[index].isOccupied = true;

            strcpy(check[index].ID,inputID);

            if(!strcmp(submitRes,"정확한풀이")) check[index].checkSolve[problemNum] = 1, check[index].countSuccess++;
            else check[index].countFailSubmit++;


            check[index].totalSubmit++;

            idlimit = index + 1;
        }

        index = 0;
        noMatch = true;

        submitCount++;

        printf(" Now On : %d\n", submitCount);
    }

    /*
        *   while + fscanf로 입력받음
        *
        *   반복문을 돌다 동일한 ID가 나오면 해당 인덱스에서 이미 푼 문제인지/제출 결과가 어떤지/몇번이나 틀렸는지 등의 정보를 저장함
        *   첫 번째 제출 기록(입력 첫줄) 처리나 처음 나오는 ID는 새로 ID를 저장하고 이후에 이미 푼 문제인지/제출 결과가 어떤지/몇번이나 틀렸는지 등의 정보를 저장함

        *   기본적인 로직은
        *   ID가 중복인지 확인 -> 이미 푼 문제인지 확인 -> 성공인지 확인(정풀) 의 과정을 거친다
    */

    fclose(readF);

    printf("\n해당 기간동안 코드업을 이용한 회원 수는 %d명으로 집계되었습니다.\n\n", idlimit);

    printAcList();

    puts("AC 순위 출력 완료!");

    printSubmitList();

    puts("소스 제출 개수 기준 순위 출력 완료!");

    printFailList();

    puts("트롤 순위 출력 완료!");

    printProblemList();
    printProblemSkipList();

    puts("많이 푼 문제 순위 출력 완료!");

    puts("");

    puts("All Done!\n\nEnjoy :)");

    fflush(stdin); getchar(); // exe 파일 바로 안 꺼지게

    return 0;
}
