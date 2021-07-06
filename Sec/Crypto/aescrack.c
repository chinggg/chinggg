#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <openssl/aes.h>
#define MAXN 16 
#define DICT "data/AES_words.txt"
#define CIPH "data/bin_cipher"

unsigned char words[32768][17];


int readwords() {
    FILE * dic = fopen(DICT, "r");
    if (dic == NULL) {
        fprintf(stderr, "Cannot read words file!");
        exit(-1);
    }
    int i = 0;
    while(~fscanf(dic, "%s", words[i])) {
        /*printf("%s\n", words[i]);*/
        i++;
    }
    fclose(dic);
    return i;
}

void readciph(unsigned char buf[]) {
    FILE * fp = fopen(CIPH, "rb");
    if (fp == NULL) {
        fprintf(stderr, "Cannot read dict file!");
        exit(-1);
    }
    fread(buf, 32, 1, fp);
    fclose(fp);
}

unsigned char* word2key(unsigned char word[]) {
    int i = 0;
    /*[0...len-1,NULL] -> [0...15,NULL]*/
    for (i = strlen(word); i < 16; i++) {
        word[i] = '#';
    }
    word[16] = '\0';
    return word;
}

int equal(unsigned char* w1, unsigned char* w2) {
    int i = 0;
    for(i=0; i<16; i++) {
        if (w1[i] != w2[i]) {
            return 0;
        }
    }
    return 1;
}

void showhex(unsigned char* v, int len) {
    for(int i=0; i<len; i++) {
        printf("%02x ", v[i]);
    }
    puts("");
}

void setiv(const unsigned char* ivs, unsigned char* ivec) {
    for (int i=0; i<MAXN && isxdigit(*ivs); i++) {
        ivec[i] = strtol(ivs+3*i, NULL, 16);
    }
}

int main(int argc, char ** argv) {
    int i;
    const unsigned char * msg = "This is a top secret.";
    unsigned char * ivs = "aa bb cc dd ee ff 00 99 88 77 66 55 44 33 22 11";
    unsigned char ivec[MAXN];
    unsigned char out[MAXN<<1];
    unsigned char cipher[MAXN<<1];
    AES_KEY enkey;
    printf("msg: %s  length: %zu\n", msg, strlen(msg));
    setiv(ivs, ivec);
    printf("ivec: ");
    showhex(ivec, 16);
    readciph(cipher);
    printf("cipher(hex): ");
    showhex(cipher, 32);
    printf("cipher(text): %s length: %d (truncated) \n", cipher, strlen(cipher));
    int num = readwords();
    printf("%d words in dict\n", num);
    unsigned char * keystr = NULL;
    for(i=0; i<num; i++) {
        setiv(ivs, ivec);
        keystr = word2key(words[i]);
        /*showhex(keystr, 16);*/
        /*printf("%s %s\n", words[i], keystr);*/
        if (strlen(keystr) != 16) {
            printf("Invalid Key!\n");
            continue;
        }
        AES_set_encrypt_key(keystr, strlen(keystr)*8, &enkey);
        AES_cbc_encrypt(msg, out, strlen(msg), &enkey, ivec, AES_ENCRYPT);
        if(equal(cipher, out)) {
            /*showhex(cipher, 32);*/
            /*showhex(out, 32);*/
            printf("%s %s\n", cipher, out);
            printf("Find key: %s", keystr);
            break;
        }
    }
    return 0;
}
