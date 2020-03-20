    .file   "solution.c"
    .text
    .globl  _darwin
    .def    _darwin;        .scl    2;      .type   32;     .endef
_darwin:
LFB17:
    .cfi_startproc
    pushl   %ebp
    .cfi_def_cfa_offset 8
    .cfi_offset 5, -8
    movl    %esp, %ebp
    .cfi_def_cfa_register 5

    movl	$-30871, %eax
    movl	$-20945, %ebx
    movl	$-14859, %ecx
    movl	$13284, %edx

    and %ecx, %ecx
    add %ebx, %ebx
    jmp n31
    add %ebx, %eax
    shr $110, %edx
    jnc n38
    jno n20
    and %ecx, %ebx
    jmp n31
    add %eax, %ebx
    shr $25, %eax
    jne n29
    cmp %edx, %edx
    jmp n31
    jnc n26
    shr $58, %ecx
    or %eax, %ecx
n20:
    cmp %edx, %ecx
    shr $112, %edx
    shr $3, %ebx
    and %ebx, %ebx
    jne n34
    shl $61, %eax
n26:
    shl $220, %ebx
    jnz n34
    xor %ebx, %ecx
n29:
    jz n36
    shr $223, %eax
n31:
    jo n33
    and %edx, %edx
n33:
    shl $148, %eax
n34:
    jnc n35
n35:
    and %ebx, %edx
n36:
    cmp %ecx, %eax
    or %eax, %ebx
n38:
    or %edx, %eax
    or %ecx, %ecx
    sub %ecx, %ebx
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
