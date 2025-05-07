#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
using namespace std;
//Eden Wilson
string getCard() {
    vector<string> cards {"Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"};
    int index= rand()%13;
    return cards.at(index);

}
void printWins(vector<int> wins) {
    cout << "Wins:" << endl;
    for (int i=0; i<wins.size(); i++) {
        if (i==0) {
            cout << "Dealer: " << wins.at(i) << endl;
        } else {
            cout << "Player "<< i << ": " << wins.at(i) << endl;
        }
    }
}
int anyOutOfMoney(vector<int> moneys) {
    int brokePerson=-1;
    for (int i=0; i<moneys.size(); i++) {
        if (moneys.at(i)<=0) {
            brokePerson=i;
        }
    }
    if (brokePerson==0) {
        //broke person is dealer
        cout << "The Dealer is broke. Game over!" << endl;
    } else if (brokePerson>0) {
        //broke person is a regular player
        cout << "Player " << brokePerson << " went broke first. Game over!" << endl;
    } else {
        //no one is broke (brokePerson = -1)
        return -1;

    }
    return brokePerson;
}
void printMoney(vector<int> moneys) {
    for (int i=0; i<moneys.size(); i++) {
        if (i==0) {
            cout << "Dealer: $";
        } else {
            cout << "Player " << i <<": $";
        }
        cout << moneys.at(i) << endl;
    }
}
int whoIsClosest(vector<int> totals) {
    //figure out who is closest to 21 without going over. return that index.
    int max=0;
    for (int i=0; i<totals.size(); i++) {
        if (totals.at(i)<=21 && totals.at(i)>max) {
            max=i;
        }
    }
    return max;
}
vector<int> getfinalPot (int winner, vector<int> bets) {
    //change everyone's bets to negative if they lost and keep the winner positive but the total of their bets
    int potTotal=0;
    for (int i=0; i<bets.size(); i++) {
        if (i!=winner) {
            potTotal+=bets.at(i);
        }
    }
    for (int i=0; i<bets.size(); i++) {
        bets.at(i)=0-bets.at(i);
    }
    bets.at(winner)=potTotal;
    return bets;

}
int checkWinner(vector<int> playerTotals) {
    int winner=-1;
    for (int i=0; i<playerTotals.size(); i++) {
        if(playerTotals.at(i)==21) {
            winner=i;
        }
    }
    return winner;

}
void printHand(vector<string> cards) {
    cout << "You have: ";
    for (string i: cards) {
        cout << i <<" ";
    }
    cout << endl;
}
int cardToValue(string cardType) {
    int aceValue;
    int value;
    if (cardType == "Ace") {
        cout << "You drew an ace! Would you like it to count as an 11 or a 1? Enter 1 or 11." << endl;
        cin >> aceValue;
        if (aceValue!=1 && aceValue!=11) {
            while (aceValue!=1 && aceValue!=11) {
                cout << "Invalid entry. Please enter 1 or 11."<< endl;
                cin >>aceValue;
            }
            
            
        }
        value=aceValue;
    } else if (cardType=="Jack" || cardType=="King" ||cardType=="Queen" || cardType=="10") {
        value = 10;
    } else {
        value = stoi(cardType);
    }
    return value;

}

vector<int> playGame(int numPlayers) {
    int winner=-1;
    string enter;
    //sample vector of what the bets might end up like. bets will be turned negative when they lose so whether they win or lose that number will only have to be added to their money total
    vector<int> temp {-20,40,-10,-10};
    
    string cardType;
    vector<vector<string>> playerHands(numPlayers);
    int cardValue;
    //set bets equal to $10 for all players
    vector<int> playerBets(numPlayers,10);
    vector<int> playerTotals(numPlayers,0);
    int toSkip[numPlayers];
    //set all values in toSkip equal to -1
    for (int &x : toSkip) {
        x=-1;
    }

   
    //Deal each player two cards
    cout << "Dealing each player two cards..." << endl;
    for (int i=0; i<numPlayers; i++) {
        if (i==0) {
            cout << "Dealer: " << endl;
        } else {
            cout << "Player " << i <<":"<< endl;
        }
        //Draw card 1
        cardType = getCard();
        (playerHands.at(i)).push_back(cardType);
        cout << "You drew a " << cardType << endl;
        cardValue = cardToValue(cardType);
        playerTotals.at(i)+=cardValue;
        //Draw Card 2
        cardType = getCard();
        (playerHands.at(i)).push_back(cardType);
        cout << "You drew a " << cardType << endl;
        cardValue = cardToValue(cardType);
        playerTotals.at(i)+=cardValue;
        //Print player total
        cout << "The total of your hand is " << playerTotals.at(i) << endl;
        cout << "Enter  \"next\" to go to the next player." << endl;
        cin >> enter;
    }
    winner=checkWinner(playerTotals);
    int turn=0;
    string choice;
    
    while (winner==-1 ) {
        //check if the toSkip list is full 
        bool foundPlayer = false;
        for (int i: toSkip) {
            if (i==-1) {
                foundPlayer=true;
            }
        }
        if (!foundPlayer) {
            cout << "Everyone has finished playing." << endl;
            winner=-2;
            break;
        }
        //Check to see if the turn needs to go back to zero after getting to the last index of the players
        if (turn>playerTotals.size()-1) {
            turn=0;
        }
        //output the player's turn
        if (turn!=0) {
            cout << "It's player " << turn << "'s turn" <<endl;
        } else {
            cout << "It's the dealer's turn " << endl;
        }
        //check if they need to be skipped 
        if (toSkip[turn]!=-1) {
            cout << "Your turn has been skipped." << endl;
            turn+=1;
            continue;
        }
        //start turn
        printHand(playerHands.at(turn));
        cout << "Your total is: " << playerTotals.at(turn) << endl;
        cout << "Would you like to hit, stay, or double? Enter h, s, or d." << endl;
        cin >> choice;
        while (choice!="h" && choice!="H" && choice!="s" && choice!="S" && choice!="d" && choice!="D") {
            cout << "Please enter a valid choice, h,s, or d to hit, stay, or double." << endl;
            cin >> choice;
            
        }
        if (choice=="h" || choice=="H") {
            //hit
            cardType = getCard();
            (playerHands.at(turn)).push_back(cardType);
            cout << "You drew a " << cardType << endl;
            cardValue = cardToValue(cardType);
            playerTotals.at(turn)+=cardValue;
            cout << "The total of your hand is " << playerTotals.at(turn) << endl;
            if (playerTotals.at(turn)>21) {
                cout << "You bust!" << endl;
                toSkip[turn]=turn;
            }
            

        } else if (choice=="s" || choice=="S") {
            //stay
            cout << "You chose to stay." << endl;
            toSkip[turn]=turn;
        } else if (choice=="d" || choice=="D") {
            //double
            cardType = getCard();
            (playerHands.at(turn)).push_back(cardType);
            cout << "You drew a " << cardType << endl;
            cardValue = cardToValue(cardType);
            playerTotals.at(turn)+=cardValue;
            playerBets.at(turn)=20;
            cout << "The total of your hand is " << playerTotals.at(turn) << endl;
            if (playerTotals.at(turn)>21) {
                cout << "You bust!" << endl;
            }
            toSkip[turn]=turn;
        }
        turn+=1;
        winner=checkWinner(playerTotals);
    }
    if (winner==-2) {
        //figure out who was the closest to 21
        winner=whoIsClosest(playerTotals);
    } 
     //change everyone's bets to negative if they lost and keep the winner positive but the total of their bets 
    //return a sample vector contianing the final numbers to be added to 
    
    return getfinalPot(winner, playerBets);
    

}


int main() {
    int numPlayers;
    srand(time(0));
    cout << "Please enter the amount of players including the dealer." << endl;
    cin >> numPlayers;
    //numPlayers=4;
    vector<int> playerMoney(numPlayers,50);
    vector<int> playerWins(numPlayers);
    vector<int> finalPot(numPlayers);
    
    
    while (anyOutOfMoney(playerMoney)==-1) {
        finalPot=playGame(numPlayers);
        int max=0;
        for (int i=0; i<finalPot.size(); i++) {
            if (finalPot.at(i)>finalPot.at(max)) {
                max=i;
            }
            playerMoney.at(i)+=finalPot.at(i);
        }

        playerWins.at(max)+=1;
        if (max==0) {
            cout << "The Dealer won!" << endl;
        } else {
            cout << "Player " << max <<" won!"<< endl;
        }
        printMoney(playerMoney);
        printWins(playerWins);
    }
    int max=0;
    for (int i=0; i<playerMoney.size(); i++) {
        if (playerMoney.at(i)>playerMoney.at(max)) {
            max=i;
        }
    }
    if (max==0) {
        cout << "The Dealer won the whole game!" << endl;
    } else {
        cout << "Player " << max <<" won the whole game!"<< endl;
    }
    printMoney(playerMoney);
    
    


}
