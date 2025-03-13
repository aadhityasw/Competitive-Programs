class Solution {
    public:
        int mostBooked(int n, vector<vector<int>>& meetings) {
            priority_queue<vector<long>, vector<vector<long>>, greater<vector<long>>> meetingRoomStatus;
            int numMeetings = meetings.size();
            sort(meetings.begin(), meetings.end());
    
            vector<int> meetingsPerRoom(n, 0);
            int numConfRoomsOccupied = 0;
    
            for (int i=0; i<numMeetings; i++) {
                long curStartTime = meetings[i][0];
                vector<int> emptyingRooms;
                while (meetingRoomStatus.size() > 0 && meetingRoomStatus.top()[0] <= curStartTime) {
                    emptyingRooms.push_back(meetingRoomStatus.top()[1]);
                    meetingRoomStatus.pop();
                }
                for (int j=0; j<emptyingRooms.size(); j++) {
                    meetingRoomStatus.push({0, emptyingRooms[j]});
                }
    
                if (meetingRoomStatus.size() == 0 || (meetingRoomStatus.top()[0] >meetings[i][0] && numConfRoomsOccupied < n)) {
                    meetingRoomStatus.push({meetings[i][1], numConfRoomsOccupied});
                    numConfRoomsOccupied++;
                }
                else {
                    long nextAvailableSlot = meetingRoomStatus.top()[0];
                    int confRoomNo = meetingRoomStatus.top()[1];
    
                    long augmentedEndTime = meetings[i][1];
                    if (nextAvailableSlot > meetings[i][0]) {
                        augmentedEndTime += (nextAvailableSlot - meetings[i][0]);
                    }
                    meetingRoomStatus.pop();
                    meetingRoomStatus.push({augmentedEndTime, confRoomNo});
                    meetingsPerRoom[confRoomNo]++;
                }
            }
    
            int curMaxNumMeetings=-1;
            int confRoomNumber = 0;
            for (int i=0; i<n; i++) {
                if (meetingsPerRoom[i] > curMaxNumMeetings) {
                    curMaxNumMeetings = meetingsPerRoom[i];
                    confRoomNumber = i;
                }
            }
    
            return confRoomNumber;
        }
    };
