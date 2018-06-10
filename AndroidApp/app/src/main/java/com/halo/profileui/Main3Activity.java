package com.halo.profileui;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Main3Activity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);
    }

    public void heSavedMe(View v) {
        Button btn = (Button) findViewById(R.id.savedBtn);
        btn.setText("Marked");
    }
}
