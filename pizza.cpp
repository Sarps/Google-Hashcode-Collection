#include <iostream>
#include <vector>

using namespace std;

typedef string CVector;
typedef vector<int> IVector;
typedef vector<IVector> IMatrix;
typedef vector<CVector> CMatrix;

void print(CMatrix m){
    for (int i=0; i<m.size(); i++) {
        cout << m[i] << endl;
    }
}

CMatrix sub_matrix(CMatrix m, int x1, int y1, int x2, int y2){
    CMatrix sub;
    for (int row=y1; row<y2; row++) {
        CVector temp = m[row].substr(x1,x2);
        sub.push_back(temp);
    }
    return sub;
}

int area (int x1, int y1, int x2, int y2) {
    return ((x2-x1+1)*(y2-y1+1));
}

bool fits_least(CMatrix orig, int x1, int y1, int x2, int y2, int l){
    CMatrix sub = sub_matrix(orig, x1, y1, x2, y2);
    int mcount=0, tcount=0;
    for (int i=0; i<sub.size(); i++) {
        for (int j=0; i<sub[i].size(); j++){
            switch(sub[i][j]){
            case 'M':
                mcount++;
                break;

            case 'T':
                tcount++;
                break;
            }
            if (tcount >= l && mcount >= l){
                return true;
            }
        }
    }
    return false;
}

vector<IMatrix> perm(CMatrix m, int nrows, int ncols, int l, int h) {
    int least = 2*l;
    cout << "least: " << least << "h: " << h << endl;;
    cout << "size: " << h-least+1 << endl;
    vector<IMatrix> result(h-least+1);
    for (int r1=0; r1<nrows; r1++ ){
        for (int c1=0; c1<ncols; c1++ ){
            for (int r2=r1; r2<nrows; r2++ ){
                for (int c2=c1; c2<ncols; c2++ ){
                    int a = area(r1,c1,r2,c2);
                    bool fits = fits_least(m,r1,c1,r2,c2,l);
                    cout << "area: " << a << fits << endl;
                    if ((a>=least && a<=h)&& fits){
                        cout << "index: " << a-least-1 << endl;
                        result[a-least].push_back({r1,c1,r2,c2});
                        cout << r1 << " " << c1 << " " << r2 << " " << c2;
                    }
                }
            }
        }
    }
    return result;
}

int main() {
    int r=3, c=5, l=1, h=6;
    CMatrix orig = {
        "TTTTT",
        "TMMMT",
        "TTTTT"
    };
    auto result = perm(orig, r, c, l, h);
    for (int i=0; i<result.size(); i++){
        for (int j=0; j<result[i].size(); j++){
            auto one_line = result[i][j];
            print(sub_matrix(orig, one_line[0], one_line[1], one_line[2], one_line[3]) );
        }
    }
}
